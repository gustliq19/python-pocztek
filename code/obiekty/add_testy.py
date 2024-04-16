from store.Apple import Apple
from store.Potato import Potato

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
