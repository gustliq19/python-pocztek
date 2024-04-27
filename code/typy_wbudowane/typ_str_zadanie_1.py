def load_person():
    name = input("Podaj swoje imie: ")
    surname = input("Podaj swoje nazwisko: ")
    name_clear = name.strip()
    surname_clear = surname.strip()

    return f"{name_clear} {surname_clear}"


def welcome():
    person = load_person()
    print(f"Nazywasz się {person}, miło Cię poznać :)")


def run():
    welcome()


if __name__ == "__main__":
    run()
