class Product:
    def __init__(self, name, category_name, price):
        self.name = name
        self.category_name = category_name
        self.price = price

    def __str__(self):
        to_print = ""
        to_print += f"Nazwa: {self.name}\n"
        to_print += f"Kategoria: {self.category_name}\n"
        to_print += f"Cena: {self.price:.2f} zł\n"

        return to_print

    def __eq__(self, other):
        if self.__class__ != other.__class__:
            return NotImplemented
        if self.name != other.name or self.category_name != other.category_name or self.price != other.price:
            return False
        return True


