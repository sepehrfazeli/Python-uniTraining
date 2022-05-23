from node import Node


class Directory(Node):

    def __init__(self, name, owner):
        super().__init__(name, owner)
        self._nodes = []

    def get_size(self):
        pass

    def get_modification_date(self):
        pass
