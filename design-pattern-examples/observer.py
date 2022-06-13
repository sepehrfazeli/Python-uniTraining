from abc import ABC, abstractmethod


class GameStop:  # Subject
    def __init__(self):
        self._subscribers = []    # observers
        self._number_of_ps5s = 0  # state

    def purchase(self, amount):
        if amount <= self._number_of_ps5s:
            self._number_of_ps5s -= amount
            return True
        else:
            return False

    def replenish(self, amount):
        is_restock = self._number_of_ps5s == 0
        self._number_of_ps5s += amount
        if is_restock:
            self.print_inventory()
            self.notify()

    def print_inventory(self):
        print(f"We have {self._number_of_ps5s} PS5s in stock!")

    def subscribe(self, subscriber):
        self._subscribers.append(subscriber)

    def notify(self):
        for subscriber in self._subscribers:
            subscriber.update(self)


class User(ABC):  # Observer
    def __init__(self, name):
        self._name = name

    @abstractmethod
    def update(self, store: GameStop):
        pass


class GreedyGamer(User):  # ConcreteObserver
    def update(self, store: GameStop):
        print(f"{self._name}: Buying PS5 NOW!!")
        store.purchase(1)  # purchase a ps5 from the store


class HesitantGamer(User):  # ConcreteObserver
    def update(self, store: GameStop):
        print(f"{self._name}: Hm, nah, waiting for a better price")


# create the store
store = GameStop()

# let some gamers subscribe
gamer1 = GreedyGamer("Hans")
store.subscribe(gamer1)

gamer2 = GreedyGamer("Xaver")
store.subscribe(gamer2)

gamer3 = HesitantGamer("Sepp")
store.subscribe(gamer3)

# fill up the inventory
store.replenish(10)
store.print_inventory()


