from node import Node


class File(Node):
    def __init__(self, size, name, owner):
        super().__init__(name, owner)
        self._size = size

    def get_size(self):
        return self._size

    def get_modification_date(self):
        return self._creation_date
