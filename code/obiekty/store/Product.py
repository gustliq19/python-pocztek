import random


class Product:
    def __init__(self, name, category_name, price):
        self.name = name
        self.category_name = category_name
        self.price = price


def print_product(product):
    print(f"Nazwa: {product.name}")
    print(f"Kategoria: {product.category_name}")
    print(f"Cena: {product.price:.2f} zł")
    print("-----")


def random_float():
    return random.randint(1, 6) + random.randint(0, 99)/100


def generate_products(orders_amount):
    products = []
    for index, product in enumerate(range(orders_amount)):
        products.append(Product(f"Produkt-{index+1}", f"kategoria-{index+1}", random_float()))
    return products
