def run():
    print_number = [lambda arg=a: arg for a in range(5)]
    print("lambda print_number", print_number[3]())

    # print_numers = lambda x: (print(i) for i in range(x))
    # print(print_numers(6))

    lambda_max = lambda a, b: a if a > b else b
    print("lambda_max:", lambda_max(5,1))



    List = [[2, 3, 4], [1, 4, 16, 64], [3, 6, 9, 12]]

    sort_list = lambda x: (sorted(i) for i in x)
    second_largest_generator = lambda x, f: (y[len(y) - 2] for y in f(x))
    second_largest = lambda x, f: [y[len(y) - 2] for y in f(x)]
    res = second_largest(List, sort_list)

    # print(type(second_largest_generator(List, sort_list)))
    for i in second_largest_generator(List, sort_list):
        print(i)
    # print(res)


if __name__ == "__main__":
    run()