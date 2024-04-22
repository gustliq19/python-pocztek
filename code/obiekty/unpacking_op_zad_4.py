from unpacking_op_zad_2 import print_kwargs


def run():
    dict1 = {
        "długość": 5,
        "wysokość": 8
    }
    print(dict1)

    dict2 = {
        "szerokość": 3,
        "gęstość": 15
    }
    print(dict2)

    dict3 = {**dict1, **dict2}
    print(dict3)

    print_kwargs(**dict3)


if __name__ == "__main__":
    run()
