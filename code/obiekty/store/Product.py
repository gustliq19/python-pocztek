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

