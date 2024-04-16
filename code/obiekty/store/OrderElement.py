class OrderElement:
    def __init__(self, product, amount):
        self.amount = amount
        self.product = product

    def print_info(self):
        print(f"Produkt:")
        self.product.print_product_info()
        print(f"Ilość: {self.amount:.2f}")
        print(f"Wartość: {self.calculate_value():.2f} zł")
        print("-----")

    def calculate_value(self):
        return self.product.price * self.amount
