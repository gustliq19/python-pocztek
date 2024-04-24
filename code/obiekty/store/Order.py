from .OrderElement import OrderElement
from .TaxCalculator import TaxCalculator
from .discount_policy import default_discount_policy


class Order:

    MAX_ORDER_ELEMENTS = 4

    def __init__(self, orderer_first_name, orderer_last_name, order_elements=None, discount=None):
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

        if discount is None:
            discount = default_discount_policy

        self.discount_policy = discount

        self._order_elements = order_elements
        self.total_price = self._calculate_total_order_value()

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
        total_price = 0
        for order_element in self._order_elements:
            total_price += order_element.value + TaxCalculator.calculate_tax_for_element(order_element)
        return self.discount_policy(total_price)

    def add_product_to_order(self, new_product, product_amount):
        if len(self._order_elements) < Order.MAX_ORDER_ELEMENTS:
            new_element = OrderElement(new_product, product_amount)
            self._order_elements.append(new_element)
            self._calculate_total_order_value()
            print(f"DODANO ELEMENT:\n{new_element}")
        else:
            print("Nie można dodać kolejnego elementu. Osiągnięto maksymalną liczbę elementów zamówienia.")

    @property
    def order_elements(self):
        return self._order_elements
