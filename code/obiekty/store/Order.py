from .Product import print_product


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
