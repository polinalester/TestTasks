import time
import random


class EmptyQueueException(Exception):
    def __init__(self):
        super().__init__("Queue is empty")


# очередь, основанная на списках
# занимает ровно столько места, сколько элементов находятся в ней в данный момент
# операция добавления в очередь имеет сложность O(1)
# (если не закончилось место в области памяти, выделенной под массив)
# операция удаления из очереди требует копирования всего массива (O(len(arr)))
class FIFO_on_list:
    def __init__(self, values=None):
        if not values:
            self.values = []
        else:
            self.values = values.copy()

    def enqueue(self, value):
        self.values.append(value)

    def dequeue(self):
        try:
            return self.values.pop()
        except IndexError:
            raise EmptyQueueException

    def __len__(self):
        return len(self.values)


# очередь, основанная на словаре
# хороший пример того, как делать не надо
# на деле она оказалась еще медленнее, чем я думала
# главное проблемное место - потребление памяти
# скорость выполнения операций тоже невысокая,
# потому что нужно высчитать место элемента в очереди
class FIFO_on_dict:
    def __init__(self, values=None):
        self.start = 0
        if not values:
            self.values = {}
            self.end = 0
        else:
            for i, v in enumerate(values):
                self.values[i] = v
            self.end = i + 1

    def enqueue(self, value):
        self.values[self.end] = value
        self.end += 1

    def dequeue(self):
        if self.start == self.end:
            raise EmptyQueueException
        value = self.values[self.start]

        del self.values[self.start]
        self.start += 1
        return value

    def __len__(self):
        return self.end - self.start


if __name__ == "__main__":
    max_int = 1000
    n_it = 1000000
    value_list = [random.randint(1, max_int) for _ in range(n_it)]

    FIFO_dict = FIFO_on_dict()
    FIFO_list = FIFO_on_list()

    start = time.time()
    for v in value_list:
        FIFO_list.enqueue(v)
    end = time.time()
    print(f"(list-based queue) enqueue: {(end-start):.7f}s")

    start = time.time()
    for _ in range(len(value_list)):
        FIFO_list.dequeue()
    end = time.time()
    print(f"(list-based queue) dequeue: {(end-start):.7f}s")

    start = time.time()
    for v in value_list:
        FIFO_dict.enqueue(v)
    end = time.time()
    print(f"(dict-based queue) enqueue: {(end-start):.7f}s")

    start = time.time()
    for _ in range(len(value_list)):
        FIFO_dict.dequeue()
    end = time.time()
    print(f"(dict-based queue) dequeue: {(end-start):.7f}s")
