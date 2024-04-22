import random

def generate_list(lenght):
    lista = []
    for i in range(lenght):
        lista.append(random.randint(4, 20))
    return lista

def run():
    lista1 = generate_list(4)
    print(lista1)
    lista2 = generate_list(2)
    print(lista2)

    lista_polaczona = [*lista1, *lista2]
    print(lista_polaczona)


if __name__ == "__main__":
    run()
