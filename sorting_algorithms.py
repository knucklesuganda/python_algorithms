import numpy


def bubble_sort(array):
    for i in range(len(array) - 1):
        for j in range(len(array) - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]

    return array


# O(n2) - bubble sort
x = numpy.random.randint(0, 100000, 100000)

print(x)
print(bubble_sort(x))
