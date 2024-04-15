class Product:
    pass


class Order:
    pass


class Apple:
    pass


class Potato:
    pass


if __name__ == "__main__":
    antonowka = Apple()
    champion = Apple()
    langrod = Apple()

    ziemniak = Potato()
    kartofel = Potato()

    print(type(antonowka))
    print(type(champion))
    print(type(langrod))

    print(type(ziemniak))
    print(type(kartofel))

    order_1 = Order()
    order_2 = Order()
    order_3 = Order()
    order_4 = Order()
    order_5 = Order()
    order_list = [order_1, order_2, order_3, order_4, order_5]

    products = {
        "jabłko": Product(),
        "winogrono": Product(),
        "marchew": Product()
    }

    print("Lista zamówień:", order_list)
    print("produkty:", products)
