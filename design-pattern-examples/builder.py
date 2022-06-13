from abc import ABC, abstractmethod


class Pizza:  # product
    def __init__(self):
        self.parts = []

    def add(self, part):
        self.parts.append(part)

    def list_ingredients(self) -> None:
        print(f"{', '.join(self.parts)}")


class PizzaChef(ABC):  # builder interface
    @abstractmethod
    def add_cheese(self):
        pass

    @abstractmethod
    def add_vegetables(self):
        pass

    @abstractmethod
    def add_meat(self):
        pass

    @abstractmethod
    def assemble(self) -> Pizza:
        pass


class ItalianPizzaChef(PizzaChef):   # builder implementation
    def __init__(self):
        self._reset()

    def _reset(self):
        self._pizza = Pizza()
        self._pizza.add("Tomato Sauce")

    def add_cheese(self):
        self._pizza.add("Mozzarella")

    def add_vegetables(self):
        self._pizza.add("Peperoni")
        self._pizza.add("Onions")
        self._pizza.add("Mushrooms")

    def add_meat(self):
        self._pizza.add("Ham")
        self._pizza.add("Seafood")

    def assemble(self) -> Pizza:
        result = self._pizza
        self._reset()
        return result


class AmericanPizzaChef(PizzaChef):  # builder implementation
    def __init__(self):
        self._reset()

    def _reset(self):
        self._pizza = Pizza()
        self._pizza.add("Ketchup")

    def add_cheese(self):
        self._pizza.add("Cheddar")

    def add_vegetables(self):
        self._pizza.add("Peppers")
        self._pizza.add("Mushrooms")

    def add_meat(self):
        self._pizza.add("Peperoni")
        self._pizza.add("Meatloaf")

    def assemble(self) -> Pizza:
        result = self._pizza
        self._reset()
        return result


class Restaurant:  # Director
    def __init__(self, chef):
        self._chef = chef

    def cook_basic_pizza(self):
        self._chef.add_cheese()
        return self._chef.assemble()

    def cook_vegetarian_pizza(self):
        self._chef.add_cheese()
        self._chef.add_vegetables()
        return self._chef.assemble()

    def cook_meat_pizza(self):
        self._chef.add_cheese()
        self._chef.add_meat()
        return self._chef.assemble()

    def cook_full_pizza(self):
        self._chef.add_cheese()
        self._chef.add_vegetables()
        self._chef.add_meat()
        return self._chef.assemble()


# create the restaurant
pizza_place = Restaurant(AmericanPizzaChef())

# create some pizzas
print(f"Basic pizza: ", end="")
pizza_place.cook_basic_pizza().list_ingredients()

print(f"Veggie pizza: ", end="")
pizza_place.cook_vegetarian_pizza().list_ingredients()

print(f"Meat pizza: ", end="")
pizza_place.cook_meat_pizza().list_ingredients()

print(f"Full pizza: ", end="")
pizza_place.cook_full_pizza().list_ingredients()
