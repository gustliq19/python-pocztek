from .products import avaliable_products
# from importowanie.zad_1.grocery_store.products import avaliable_products

all_orders = []

# TODO funkcja sprawdzajaca czy podany produkt jest w magazynie

def make_order(product_name, demanted_amount):

    avaliable_amount = avaliable_products[product_name]["ilość"]
    if demanted_amount > avaliable_amount:
        print(f"Nie jest dostępna żądana ilość produktu {product_name.upper()}. Do zamówienia dodano {avaliable_amount} szt.")
        order_amount = avaliable_amount
    else:
        order_amount = demanted_amount

    # odejmowanie dostępnej ilość produków z magazynu
    # TODO uzyc funkcji odejmującej
    avaliable_products[product_name]["ilość"] -= order_amount

    order_cost = avaliable_products[product_name]["cena"] * order_amount

    new_order = {
        "nazwa_produktu": product_name,
        "ilość": order_amount,
        "koszt": order_cost
    }

    all_orders.append(new_order)
    return new_order
