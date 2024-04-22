class Product:
    def __init__(self, name, category_name, price):
        self.name = name
        self.category_name = category_name
        self.price = price

    def __str__(self):
        to_print = f"{self.name} [{self.category_name}] | "
        # to_print += f"Nazwa: {self.name}\n"
        # to_print += f"Kategoria: {self.category_name}\n"
        to_print += f"Cena: {self.price:.2f} zł"

        return to_print

    def __eq__(self, other):
        if self.__class__ != other.__class__:
            return NotImplemented
        return self.name == other.name and self.category_name == other.category_name and self.price == other.price
