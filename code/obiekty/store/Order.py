import random
from .Product import Product
from .OrderElement import OrderElement
from .TaxCalculator import TaxCalculator


class Order:

    MAX_ORDER_ELEMENTS = 4

    def __init__(self, orderer_first_name, orderer_last_name, order_elements=None):
        self.orderer_last_name = orderer_last_name
        self.orderer_first_name = orderer_first_name
        self.total_price = 0

        if order_elements is None:
            order_elements = []
        elif len(order_elements) > Order.MAX_ORDER_ELEMENTS:
            print(f"Zamówienie {self.orderer_first_name.upper()} {self.orderer_last_name.upper()} --> ", end="")
            print(f"Przekroczono maksymalną liczbę elementów zamówienia. ", end="")
            print(f"Dodano {Order.MAX_ORDER_ELEMENTS} pierwszych elementów.")

            order_elements = order_elements[:Order.MAX_ORDER_ELEMENTS]

        self._order_elements = order_elements
        self._calculate_total_order_value()

    def __str__(self):
        to_print = ""
        to_print += f"Zamawiający: {self.orderer_first_name} {self.orderer_last_name}\n"
        to_print += f"Elementy zamówienia:\n"
        for order_element in self._order_elements:
            to_print += "\t" + str(order_element)

        to_print += f"Wartość całkowita: {self.total_price:.2f} zł BRUTTO\n"

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
        self.total_price = 0
        for order_element in self._order_elements:
            # self.total_price += order_element.calculate_value()
            self.total_price += order_element.calculate_value() + TaxCalculator.calculate_tax_for_element(order_element)

    def add_product_to_order(self, new_product, product_amount):
        if len(self._order_elements) < Order.MAX_ORDER_ELEMENTS:
            new_element = OrderElement(new_product, product_amount)
            self._order_elements.append(new_element)
            self._calculate_total_order_value()
            print(f"DODANO ELEMENT:\n{new_element}")
        else:
            print("Nie można dodać kolejnego elementu. Osiągnięto maksymalną liczbę elementów zamówienia.")

    @classmethod
    def _random_float(cls):
        return random.randint(1, 6) + random.randint(0, 99)/100

    @classmethod
    def generate_order_elements(cls, elements_amount):
        random_order_elements = []
        for index, product in enumerate(range(elements_amount)):
            new_product = Product(f"Produkt-{index+1}", f"kategoria-{index+1}", price=cls._random_float())
            random_order_elements.append(OrderElement(new_product, amount=cls._random_float()))
        return random_order_elements
