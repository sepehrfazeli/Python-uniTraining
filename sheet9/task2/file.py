from node import Node


class File(Node):
    def __init__(self, size, name, owner):
        super().__init__(name, owner)
        self.size = size

    def get_modification_date(self):
        pass

    def get_size(self):
        pass
