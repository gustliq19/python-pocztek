def load_colors():
    return input("Podaj swoje ulubione kolory (oddzielone przecinkiem): ")


def is_in_str(source, to_find):
    if source.find(to_find) != -1:
        print(f"Kolor {to_find.upper()} znajduje się na Twojej liście")
    else:
        print(f"Koloru {to_find.upper()} nie ma na Twojej liście")


def run():
    colors = load_colors()
    is_in_str(colors, "niebieski")


if __name__ == "__main__":
    run()
