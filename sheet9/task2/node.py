from datetime import datetime
from abc import abstractmethod


class Node:
    def __init__(self, name, owner):
        self.name = name
        self.owner = owner
        self.creation_date = datetime.now()

    @abstractmethod
    def get_size(self):
        pass

    @abstractmethod
    def get_modification_date(self):
        pass

    def __str__(self):
        date_time_format = ""

    def print_attributes(self):
        print(f"name : {self.name}\n"
              f"owner : {self.owner}\n"
              f"creation_date : {self.creation_date}")


