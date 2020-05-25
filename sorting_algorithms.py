import numpy


def bubble_sort(array):
    for i in range(len(array) - 1):
        for j in range(len(array) - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]

    return array
# O(n2) - bubble sort


def insertion_sort(array):
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1

        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j -= 1

        array[j + 1] = key

    return array

# O(n2) - bad insertion sort
# O(n) - best insertion sort


x = numpy.random.randint(0, 100, 100)

print(x)
print(insertion_sort(x))
