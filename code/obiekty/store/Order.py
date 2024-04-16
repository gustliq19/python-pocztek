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

    def print_order(self):
        print(f"Zamawiający: {self.orderer_first_name} {self.orderer_last_name}")
        print(f"Produkty:")
        for product in self.products:
            product.print_product()

        print(f"Cena całkowita: {self.total_price:.2f} zł")
