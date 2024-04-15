from store import Order
from store.Order import print_orders
from store.Product import generate_products

if __name__ == "__main__":

    order_1 = Order.Order("Tomasz", "Morawski", generate_products(3))
    order_2 = Order.Order("Jan", "Kowalski", generate_products(5))
    order_3 = Order.Order("Piotr", "Górski", generate_products(6))
    order_list = [order_1, order_2, order_3]

    print("Lista zamówień:\n\n")
    print_orders(order_list)
