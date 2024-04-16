class Product:
    def __init__(self, name, category_name, price):
        self.name = name
        self.category_name = category_name
        self.price = price

    def print_product_info(self):
        print(f"Nazwa: {self.name}")
        print(f"Kategoria: {self.category_name}")
        print(f"Cena: {self.price:.2f} zł")
