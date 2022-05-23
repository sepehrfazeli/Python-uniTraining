from node import Node


class Directory(Node):

    def __init__(self, name, owner):
        super().__init__(name, owner)
        self._nodes = []

    def add(self, node: Node):
        self._nodes.append(node)

    def remove(self, node: Node):
        self._nodes.remove(node)

    def get_size(self):
        total_size = 0
        for node in self._nodes:
            node_size = node.get_size()
            total_size += node_size
        return total_size

    def get_modification_date(self):
        most_recent_date = self._creation_date
        for node in self._nodes:
            node_date = node.get_modification_date()
            if node_date > most_recent_date:
                most_recent_date = node_date
        return most_recent_date

    def list(self):
        for node in self._nodes:
            print(node)
