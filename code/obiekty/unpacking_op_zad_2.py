def print_kwargs(**kwargs):
    print("(", end="")
    for key, value in kwargs.items():
        print(f"{key}={value}", end=", ")
    print(")", end="")


if __name__ == "__main__":
    print_kwargs(imie="Tomasz", nazwisko="Morawski", wiek=26)