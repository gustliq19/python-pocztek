from grocery_store.actions import make_order, all_orders


def run_grocery_store():
    # TODO wypisz stan magazynu

    while True:
        product_name = input("Podaj nazwę zamawianego produktu, lub wpisz 'x' aby zakończyć: ")
        # TODO sprawwdzenie czy produkt o takiej nazwie istnieje
        if product_name == 'x':
            break
        amount = int(input("Podaj ilość: "))

        all_orders.append(make_order(product_name, amount))

    # TODO napisać funkcje, która będzie wypisywała skład nowego zamówienia grupując te same produkty
    print("\nTwoje zamówienie składa się z:")
    for order in all_orders:
        print(f'{order["nazwa_produktu"].upper()} w ilości: {order["ilość"]} ---- koszt to: {order["koszt"]:.2f} zł')

    total_products_cost = 0
    for order in all_orders:
        total_products_cost += order["koszt"]

    print(f"Całkowita kwota do zapłaty to {total_products_cost:.2f} zł")


if __name__ == "__main__":
    run_grocery_store()