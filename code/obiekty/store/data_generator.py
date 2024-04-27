from .Product import Product
from .OrderElement import OrderElement
from .Order import Order
import random

MIN_PRODUCT_PRICE = 1
MAX_PRODUCT_PRICE = 6
MIN_PRODUCT_AMOUNT = 4
MAX_PRODUCT_AMOUNT = 7


def random_float(a, b):
    return round(random.uniform(a, b), ndigits=2)
    # return random.randint(a, b) + random.randint(0, 99) / 100


def generate_order_elements(elements_amount=None):
    if elements_amount is None:
        elements_amount = random.randint(1, Order.MAX_ORDER_ELEMENTS)
    random_order_elements = []
    for index, product in enumerate(range(elements_amount)):
        new_product = Product(f"Produkt-{index + 1}", f"kategoria-{index + 1}", price=random_float(MIN_PRODUCT_PRICE, MAX_PRODUCT_PRICE))
        random_order_elements.append(OrderElement(new_product, amount=random_float(MIN_PRODUCT_AMOUNT, MAX_PRODUCT_AMOUNT)))
    return random_order_elements
