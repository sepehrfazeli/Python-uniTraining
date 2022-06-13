from collections.abc import Iterable, Iterator


# Iterator = Iterator
# ConcreteIterator = AlphabeticOrderIterator
class AlphabeticOrderIterator(Iterator):
    def __init__(self, item: str):
        self._ordered_chars = sorted(item)
        self._length = len(self._ordered_chars)
        self._position = 0

    def __next__(self):
        if self._position == self._length:
            raise StopIteration
        next_item = self._ordered_chars[self._position]
        self._position += 1
        return next_item


# Aggregate = Iterable
# ContcreteAgregate = OrderedString
class OrderedString(Iterable):
    def __init__(self, unordered_string: str):
        self._unordered_string = unordered_string

    def __iter__(self):
        return AlphabeticOrderIterator(self._unordered_string)


ordered_string = OrderedString("hello world")
for char in ordered_string:
    print(char, end="")
