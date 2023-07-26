def input_data() -> tuple:
    """
    Функция ввода данных.
    """
    ver_A = [int(i) for i in input().split('.')]
    ver_B = [int(i) for i in input().split('.')]
    return ver_A, ver_B


def compare_versions(ver_a: list, ver_b: list) -> int:
    """
    Функция сравнения версий.
    """
    while not len(ver_a) == len(ver_b):
        if len(ver_a) < len(ver_b):
            ver_a.append(0)
            continue
        ver_b.append(0)
    for i, el in enumerate(ver_a):
        if ver_a[i] > ver_b[i]:
            return 1
        if ver_a[i] < ver_b[i]:
            return -1
    return 0


def main() -> None:
    """
    Главная функция.
    """
    ver_a, ver_b = input_data()
    print(compare_versions(ver_a, ver_b))


if __name__ == '__main__':
    main()
