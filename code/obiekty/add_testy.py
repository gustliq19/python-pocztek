from store.Apple import Apple
from store.Potato import Potato
from store.Product import Product
from store.OrderElement import OrderElement
from store.Order import Order

apple = Apple("Champion", "duże", 2.71)
red_apple = Apple("Langrod", "duże", 3.14)
potato = Potato("na frytki", "długi", 1.31)

print("JABŁKO: ", end="")
apple.print()
print("CZERW. JABŁKO: ", end="")
red_apple.print()
print("ZIEMNIAK: ", end="")
potato.print()

# added_apple = apple + 4
# print("apple + 4: ", end="")
# added_apple.print()

added_apple = apple + potato
print("apple + 4: ", end="")
added_apple.print()

print(repr(apple))
print(repr(potato))

banan = Product("banan", "owoc", 2.15)
jablko = Product("jabłko", "owoc", 1.35)
gruszka = Product("gruszka", "owoc", 3.44)
print("product1 == product2:", banan == jablko)

order_elem1 = OrderElement(banan, 12)
order_elem2 = OrderElement(jablko, 12)
order_elem3 = OrderElement(gruszka, 2)
print("order_elem1 == order_elem2:", order_elem1 == order_elem2)

elements1 = [
    OrderElement(banan, 5),
    OrderElement(jablko, 12)
    # OrderElement(gruszka, 6)
]
elements2 = [
    OrderElement(jablko, 12),
    OrderElement(banan, 5)
]
order1 = Order("Tomasz", "Morawski", elements1)
order2 = Order("Tomasz", "Morawski", elements2)
# order2.orderer_first_name = "Damian"
print("order1 == order2:", order1 == order2)
print(OrderElement(jablko, 12) in elements1)
# print(order_elem2 == order_elem3)

