import json
import xml.etree.ElementTree as elementTree
from abc import ABC


class Song:
    def __init__(self, title, artist):
        self.title = title
        self.artist = artist

    def serialize(self, serializer):
        serializer.start_object('song')
        serializer.add_property('title', self.title)
        serializer.add_property('artist', self.artist)
        return serializer.to_str()


class Serializer(ABC):  # Product
    def start_object(self, object_name):
        pass

    def add_property(self, name, value):
        pass

    def to_str(self):
        pass


class SerializerFactory:  # Creator
    def __init__(self):
        self._creators = {}

    def register_format(self, format_name, creator: Serializer):
        self._creators[format_name] = creator

    def get_serializer(self, format_name):  # factory method
        creator = self._creators.get(format_name)
        if not creator:
            raise ValueError(format_name)
        return creator()


class JsonSerializer(Serializer):  # Concrete Creator
    def __init__(self):
        self._current_object = None

    def start_object(self, object_name):
        self._current_object = {}

    def add_property(self, name, value):
        self._current_object[name] = value

    def to_str(self):
        return json.dumps(self._current_object)


class XmlSerializer(Serializer):  # Concrete Creator
    def __init__(self):
        self._element = None

    def start_object(self, object_name):
        self._element = elementTree.Element(object_name)

    def add_property(self, name, value):
        prop = elementTree.SubElement(self._element, name)
        prop.text = value

    def to_str(self):
        return elementTree.tostring(self._element, encoding='unicode')


factory = SerializerFactory()
factory.register_format('JSON', JsonSerializer)
factory.register_format('XML', XmlSerializer)


def repl():  # read evaluate print loop
    print("Welcome to the awesome song serializer!")
    enter_song = True
    while enter_song:
        song, format_name = ask_song_info()
        print_song(song, format_name)
        enter_song = ask_continue()
    print("ByeBye!")


def ask_song_info():
    print("Enter the artist")
    artist = input()
    print("Enter the title")
    title = input()
    song = Song(artist, title)
    print("Enter the output format")
    format_name = input()
    return song, format_name


def print_song(song, format_name):
    serializer = factory.get_serializer(format_name)
    print(song.serialize(serializer))


def ask_continue():
    print("Continue? (Y/N)")
    cont = input()
    return cont == "Y"


repl()
