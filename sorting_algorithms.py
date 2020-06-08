
def bubble_sort(array, reversed_order=False):
    operation = "array[i] > array[j]"

    if reversed_order:
        operation = "array[i] < array[j]"

    for i in range(len(array)):
        for j in range(len(array)):
            if eval(operation):
                array[i], array[j] = array[j], array[i]

    return array


print(bubble_sort([-5, 6, 1, 4, 0], True))
# O(n2) - bubble sort
