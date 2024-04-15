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


if __name__ == "__main__":

    order_1 = Order("Tomasz", "Morawski", [
                                        Product("jabłko", "owoc", 2.8),
                                        Product("gruszka", "owoc", 1.38),
                                        Product("jabłko", "owoc", 3.21)])
    order_2 = Order("Jan", "Kowalski", [
                                        Product("marchew", "warzywo", 1.31),
                                        Product("gruszka", "owoc", 1.38)])
    order_3 = Order("Piotr", "Górski", [
                                        Product("jabłko", "owoc", 2.8),
                                        Product("zamniak", "warzywo", 2.41),
                                        Product("ananas", "owoc", 5.79),
                                        Product("arbuz", "owoc", 6.70)])
    order_list = [order_1, order_2, order_3]

    print("Lista zamówień:\n\n")
    print_orders(order_list)
