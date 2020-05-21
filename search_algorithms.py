from random import randint
import datetime
import numpy


def find_num(array, key):
    for i in range(len(array)):
        if array[i] == key:
            return i

    return -1


def binary_search(array, key):
    lower_bound = 0
    upper_bound = len(array) - 1

    while lower_bound <= upper_bound:
        center = (lower_bound + upper_bound) // 2

        if array[center] == key:
            return center

        elif array[center] > key:
            upper_bound = center - 1
        elif array[center] < key:
            lower_bound = center + 1

    return -1


# O(n) - linear search
# O(log(n)) - binary search

x = numpy.random.randint(0, 10000, 100000)

print("Array created")

x = sorted(x)
print("Array sorted")

start = datetime.datetime.now()
print(find_num(x, 1023))
print("End time:", datetime.datetime.now() - start)
