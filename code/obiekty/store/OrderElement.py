from .TaxCalculator import TaxCalculator


class OrderElement:
    def __init__(self, product, amount):
        self.amount = amount
        self.product = product
        self.value = self.calculate_value()

    def __str__(self):
        to_print = ""
        # to_print += f"Produkt:\n"
        to_print += str(self.product)
        to_print += f" | Ilość: {self.amount:.2f} | "
        to_print += f"Wartość: {self.value:.2f} zł NETTO ; {(self.value + TaxCalculator.calculate_tax_for_element(self)):.2f} zł BRUTTO\n"
        # to_print += "-----\n"

        return to_print

    def __eq__(self, other):
        if self.__class__ != other.__class__:
            return NotImplemented
        return self.amount == other.amount and self.product == other.product

    def calculate_value(self):
        return self.product.price * self.amount
