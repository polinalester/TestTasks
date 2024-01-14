import time
import random


N_LIM = 1000000
N_IT = 100000


# стандартная функция для определения четности,
# которая используется практически везде
# легко читаемая и понятная большинству программистов
# небольшие временные и ресурсные затраты
def isEven(value):
    return value % 2 == 0


# самая неэффективная структура данных, много лишних преобразований и операторов
# с первого раза трудно понять, что делает функция
# в разы медленнее первого способа
# может быть понятнее людям, незнакомым с операторами % и &
def isEven_str(value):
    return any(str(value).endswith(str(n)) for n in range(0, 9, 2))


# работает с бинарным представлением числа, поэтому немного быстрее,
# чем предыдущая
# все равно присутствуют лишние преобразования
def isEven_bin_str(value):
    return bin(value).endswith("0")


# использует "родное" бинарное представление числа"
# и оптимизированную бинарную операцию
# по скорости приближается к первой функции
# более "нестандартная", менее узнаваемая, чем первая функция
def isEven_bin(value):
    return not bool(1 & value)


def time_func(func, params):
    start = time.time()
    for p in params:
        func(p)
    end = time.time()
    return end-start


if __name__ == "__main__":
    for n in [0, 6, 124, 890]:
        assert isEven(n)
        assert isEven_str(n)
        assert isEven_bin_str(n)
        assert isEven_bin(n)

    for n in [1, 7, 255, 1033]:
        assert not isEven(n)
        assert not isEven_str(n)
        assert not isEven_bin_str(n)
        assert not isEven_bin(n)

    params = [random.randint(0, N_LIM) for _ in range(N_IT)]
    print("isEven:".ljust(15), time_func(isEven, params))
    print("isEven_str:".ljust(15), time_func(isEven_str, params))
    print("isEven_bin_str:".ljust(15), time_func(isEven_bin_str, params))
    print("isEven_bin:".ljust(15), time_func(isEven_bin, params))
