from datetime import datetime
from abc import abstractmethod


class Node:
    def __init__(self, name, owner):
        self._name = name
        self._owner = owner
        self._creation_date = datetime.now()

    @abstractmethod
    def get_size(self):
        pass

    @abstractmethod
    def get_modification_date(self):
        pass

    def __str__(self):
        date_time_format = "%d/%m/%Y %H:%M:%S"

        creation_date_formatted = self._creation_date.strftime(date_time_format)
        modification_date_formatted = self.get_modification_date().strftime(date_time_format)

        return f"name : {self._name} " \
               f"owner : {self._owner} " \
               f"size : {self.get_size()}" \
               f"creation_date : {creation_date_formatted}" \
               f"modification_date : {modification_date_formatted}"
