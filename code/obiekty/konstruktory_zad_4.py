from store.Order import Order
from store.Product import generate_products
from store.Apple import Apple
from store.Potato import Potato

if __name__ == "__main__":

    order_1 = Order("Tomasz", "Morawski", generate_products(3))
    order_2 = Order("Jan", "Kowalski", generate_products(5))
    order_3 = Order("Piotr", "Górski", generate_products(6))
    order_list = [order_1, order_2, order_3]

    print("Lista zamówień:\n\n")
    for order in order_list:
        order.print_order()

    red_apple = Apple("champion", "duże", 2.18)
    old_potato = Potato("na frytki", "długi", 1.35)

    apple_kg_amount = 2.5
    potato_kg_amount = 3.74

    print()
    red_apple.print()
    old_potato.print()
    print(f"Cena {apple_kg_amount} kg jabłek wynosi: {red_apple.calculate_price(apple_kg_amount):.2f} zł")
    print(f"Cena {potato_kg_amount} kg jabłek wynosi: {red_apple.calculate_price(potato_kg_amount):.2f} zł")
