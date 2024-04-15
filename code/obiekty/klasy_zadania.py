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
                self.total_price += product.kg_price

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


def print_orders(orders):
    for order in orders:
        print(f"Zamawiający: {order.orderer_first_name} {order.orderer_last_name}")
        print(f"Produkty:")
        for product in order.products:
            print(f"Nazwa: {product.species_name} | Cena: {product.kg_price:.2f} zł")
        print(f"Cena całkowita: {order.total_price:.2f} zł")
        print()

def print_products(products):
    for name, product in products.items():
        print(f"Nazwa: {name} [{product.name}]")
        print(f"Kategoria: {product.category_name}")
        print(f"Cena: {product.price:.2f} zł")
        print()


if __name__ == "__main__":
    antonowka = Apple("antonówka", "małe", 2.38)
    champion = Apple("champion", "duże", 3.21)
    langrod = Apple("langrod", "średnie", 2.57)

    ziemniak = Potato("dobry", "mały", 1.45)
    kartofel = Potato("lepszy", "duży", 1.78)

    print(type(antonowka))
    print(type(champion))
    print(type(langrod))

    print(type(ziemniak))
    print(type(kartofel))

    order_1 = Order("Tomasz", "Morawski", [antonowka, antonowka, champion])
    order_2 = Order("Jan", "Kowalski", [champion, kartofel])
    order_3 = Order("Piotr", "Górski", [antonowka, antonowka, ziemniak, ziemniak, ziemniak])
    order_4 = Order("Ewelina", "Jagódka", [langrod, langrod, champion])
    order_5 = Order("Ryszard", "Brzoza", [antonowka, kartofel, kartofel, langrod])
    order_list = [order_1, order_2, order_3, order_4, order_5]

    products = {
        "jabłko": Product("lobo", "owoc", 2.50),
        "winogrono": Product("słodkie", "owoc", 4.18),
        "marchew": Product("długa", "warzywo", 1.32)
    }

    print("Lista zamówień:")
    print_orders(order_list)
    print()
    print("Przykładowe produkty:")
    print_products(products)
