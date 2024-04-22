def make_string(*args):
    string = ""
    for s in args:
        string += str(s) + "-"
    return string[:-1]


if __name__ == "__main__":
    print(make_string(12, 3, "napis", "inny napis"))
