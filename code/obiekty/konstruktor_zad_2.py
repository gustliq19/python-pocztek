import random

class Product:
    def __init__(self, name, category_name, price):
        self.name = name
        self.category_name = category_name
        self.price = price


class Order:
    def __init__(self, orderer_first_name, orderer_last_name, products=None):
        self.orderer_last_name = orderer_last_name
        self.orderer_first_name = orderer_first_name
        self.total_price = 0

        if products is None:
            products = []
        else:
            for product in products:
                self.total_price += product.price

        self.products = products


class Apple:
    def __init__(self, species_name, size, kg_price):
        self.species_name = species_name
        self.size = size
        self.kg_price = kg_price


class Potato:
    def __init__(self, species_name, size, kg_price):
        self.species_name = species_name
        self.size = size
        self.kg_price = kg_price


def print_product(product):
    print(f"Nazwa: {product.name}")
    print(f"Kategoria: {product.category_name}")
    print(f"Cena: {product.price:.2f} zł")
    print("-----")


def print_order(order):
    print(f"Zamawiający: {order.orderer_first_name} {order.orderer_last_name}")
    print(f"Produkty:")
    for product in order.products:
        print_product(product)
    print(f"Cena całkowita: {order.total_price:.2f} zł")


def print_orders(orders):
    for order in orders:
        print_order(order)
        print()


def random_float():
    return random.randint(1,6) + random.randint(0,99)/100


def generate_products(orders_amount):
    products = []
    for index, product in enumerate(range(orders_amount)):
        products.append(Product(f"Produkt-{index+1}", f"kategoria-{index+1}", random_float()))
    return products


if __name__ == "__main__":

    order_1 = Order("Tomasz", "Morawski", generate_products(3))
    order_2 = Order("Jan", "Kowalski", generate_products(5))
    order_3 = Order("Piotr", "Górski", generate_products(6))
    order_list = [order_1, order_2, order_3]

    print("Lista zamówień:\n\n")
    print_orders(order_list)
