import random
from .Product import Product
from .OrderElement import OrderElement


class Order:
    def __init__(self, orderer_first_name, orderer_last_name, order_elements=None):
        self.orderer_last_name = orderer_last_name
        self.orderer_first_name = orderer_first_name
        self.total_price = 0

        if order_elements is None:
            order_elements = []

        self._order_elements = order_elements
        self._calculate_total_order_value()

    def __str__(self):
        to_print = ""
        to_print += f"Zamawiający: {self.orderer_first_name} {self.orderer_last_name}\n"
        to_print += f"Elementy zamówienia:\n"
        for order_element in self._order_elements:
            to_print += str(order_element)

        to_print += f"Wartość całkowita: {self.total_price:.2f} zł\n"

        return to_print

    def __len__(self):
        return len(self._order_elements)

    def __eq__(self, other):
        if self.__class__ != other.__class__:
            return NotImplemented
        if self.orderer_first_name != other.orderer_first_name or self.orderer_last_name != other.orderer_last_name:
            return False
        if len(self) != len(other):
            return False
        for order_element in self._order_elements:
            if order_element not in other._order_elements:
                return False
        return True

    def _calculate_total_order_value(self):
        for order_element in self._order_elements:
            self.total_price += order_element.calculate_value()

    def add_product_to_order(self, new_product, product_amount):
        new_element = OrderElement(new_product, product_amount)
        self._order_elements.append(new_element)
        self._calculate_total_order_value()


def random_float():
    return random.randint(1, 6) + random.randint(0, 99)/100


def generate_order_elements(elements_amount):
    random_order_elements = []
    for index, product in enumerate(range(elements_amount)):
        new_product = Product(f"Produkt-{index+1}", f"kategoria-{index+1}", price=random_float())
        random_order_elements.append(OrderElement(new_product, amount=random_float()))
    return random_order_elements
