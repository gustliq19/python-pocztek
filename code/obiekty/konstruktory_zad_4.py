from store.Order import Order
from store.OrderElement import OrderElement
from store.Apple import Apple
from store.Potato import Potato
from store.Product import Product

if __name__ == "__main__":

    # order_1 = Order("Tomasz", "Morawski", Order.generate_order_elements(3))
    # order_2 = Order("Jan", "Kowalski", Order.generate_order_elements(5))
    # order_3 = Order("Piotr", "Górski", Order.generate_order_elements(6))
    # order_list = [order_1, order_2, order_3]

    gruszka = Product("gruszka", "Owoce i warzywa", 3.14)
    banan = Product("banan", "Owoce i warzywa", 2.06)
    chleb = Product("chleb", "Jedzenie", 1.38)
    cukierki = Product("cukierki", "Słodycze", 5.19)
    ciastka = Product("ciastka", "Słodycze", 4.15)

    order_1 = Order("Tomasz", "Morawski", [
        OrderElement(gruszka, 2.7),
        OrderElement(banan, 5),
        OrderElement(cukierki, 1.56)
    ])

    order_2 = Order("Jan", "Kowalski", [
        OrderElement(ciastka, 1.2),
        OrderElement(chleb, 2),
        OrderElement(cukierki, 1.56)
    ])

    order_3 = Order("Piotr", "Górski", [
        OrderElement(banan, 5),
        OrderElement(chleb, 2),
        OrderElement(gruszka, 4.5)
    ])
    order_list = [order_1, order_2, order_3]

    print("Lista zamówień:\n")
    for order in order_list:
        print(order)

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
