from store.Order import Order
from store.Product import generate_products

if __name__ == "__main__":

    order_1 = Order("Tomasz", "Morawski", generate_products(3))
    order_2 = Order("Jan", "Kowalski", generate_products(5))
    order_3 = Order("Piotr", "Górski", generate_products(6))
    order_list = [order_1, order_2, order_3]

    print("Lista zamówień:\n\n")
    for order in order_list:
        order.print_order()
