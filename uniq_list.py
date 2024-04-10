def uniq_function(a: list[any]) -> list[any]:
    return list(dict.fromkeys(a))


def uniq1_function(a: list[any]) -> list[any]:
    return list(set(a))


date = [1, 2, 1, 2, 3, 4, 4, 5,]


if __name__ == '__main__':
    print(uniq_function(date))
    print(uniq1_function(date))
