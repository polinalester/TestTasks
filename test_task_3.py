import time
import random


# посколько входных данных маловато, выбрала стандартный mergesort
# у него одинаковая сложность в самом легком, среднем и самом сложном случае (O(nlogn)),
# поэтому он не зависит от входных данных (от их степени отсортированности)
# главный недостаток - необходимость поддержания двух массивов одновременно
# (требуется вдвое больше памяти, не подойдет для ситуаций, массив большой)
def merge_sort(arr):
    if len(arr) == 1:
        return arr
    else:
        mid = len(arr)//2

        left = merge_sort(arr[:mid])
        right = merge_sort(arr[mid:])

        i_l = 0
        i_r = 0
        temp_arr = []

        while i_l < len(left) and i_r < len(right):
            if left[i_l] < right[i_r]:
                temp_arr.append(left[i_l])
                i_l += 1
            else:
                temp_arr.append(right[i_r])
                i_r += 1

        for i in range(i_l, len(left)):
            temp_arr.append(left[i])

        for i in range(i_r, len(right)):
            temp_arr.append(right[i])

        return temp_arr


def validate_sort(init_arr, sorted_arr):
    assert len(init_arr) == len(sorted_arr)
    for i in range(0, len(sorted_arr)-1):
        assert sorted_arr[i] <= sorted_arr[i+1]


if __name__ == "__main__":
    max_int = 100000
    for arr_len in [10, 999, 10000, 1000023, 10000000]:
        arr_to_sort = [random.randint(0, max_int) for _ in range(arr_len)]

        start = time.time()
        sorted_arr = merge_sort(arr_to_sort)
        end = time.time()

        print(f"array length: {arr_len}, time: {(end-start):.7f}s")

        validate_sort(arr_to_sort, sorted_arr)
