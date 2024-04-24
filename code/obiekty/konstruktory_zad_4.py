from store.Order import Order
from store.OrderElement import OrderElement
from store.Apple import Apple
from store.Potato import Potato
from store.Product import Product
from store.discount_policy import christmas_discount, loyal_customer_discount
from store import data_generator


def run():
    # order_1 = Order("Tomasz", "Morawski", data_generator.generate_order_elements(3), discount=loyal_customer_discount)
    # order_2 = Order("Jan", "Kowalski", data_generator.generate_order_elements(5))
    # order_3 = Order("Piotr", "Górski", data_generator.generate_order_elements(6))
    # order_4 = Order("Wiesław", "Zszywka", data_generator.generate_order_elements(2))
    # order_5 = Order("Antoni", "Traczyk", data_generator.generate_order_elements(4))
    # order_list = [order_1, order_2, order_3, order_4, order_5]

    gruszka = Product("gruszka", "Owoce i warzywa", 3.14)
    banan = Product("banan", "Owoce i warzywa", 2.06)
    chleb = Product("chleb", "Jedzenie", 1.38)
    cukierki = Product("cukierki", "Słodycze", 5.19)
    ciastka = Product("ciastka", "Słodycze", 4.15)

    order_0 = Order("Albert", "Einstain", discount=loyal_customer_discount)
    print(order_0)
    order_0.order_elements = [
        OrderElement(gruszka, 2.7),
        OrderElement(banan, 5),
        OrderElement(cukierki, 1.56),
        OrderElement(chleb, 3),
        OrderElement(ciastka, 2)
    ]
    print(order_0)
    order_0.order_elements = [
        OrderElement(ciastka, 1.2),
        OrderElement(chleb, 2),
        OrderElement(cukierki, 20)
    ]
    print(order_0)

    order_1 = Order("Tomasz", "Morawski", [
        OrderElement(gruszka, 2.7),
        OrderElement(banan, 5),
        OrderElement(cukierki, 1.56)
    ], discount=loyal_customer_discount)

    order_2 = Order("Jan", "Kowalski", [
        OrderElement(ciastka, 1.2),
        OrderElement(chleb, 2),
        OrderElement(cukierki, 20)
    ], discount=christmas_discount)

    order_3 = Order("Piotr", "Górski", [
        OrderElement(banan, 5),
        OrderElement(chleb, 2),
        OrderElement(gruszka, 4.5)
    ])
    order_list = [order_1, order_2, order_3]

    for order in order_list:
        print(order)

    # sortowanie listy zamówień

    order_list.sort(key=lambda order: order.total_price)
    print("=" * 30)

    for order in order_list:
        print(order)

    # wypisanie wszystkich elementów danego zamowienia
    print("=" * 40)
    for order_element in order_2.order_elements:
        print(order_element)
    print("=" * 40)

    red_apple = Apple("champion", "duże", 2.18)
    old_potato = Potato("na frytki", "długi", 1.35)

    apple_kg_amount = 2.5
    potato_kg_amount = 3.74

    print()
    order_1.add_product_to_order(ciastka, 1)
    print(order_1)

    # red_apple.print()
    # old_potato.print()
    # print(f"Cena {apple_kg_amount} kg jabłek wynosi: {red_apple.calculate_price(apple_kg_amount):.2f} zł")
    # print(f"Cena {potato_kg_amount} kg jabłek wynosi: {red_apple.calculate_price(potato_kg_amount):.2f} zł")


if __name__ == "__main__":
    run()
