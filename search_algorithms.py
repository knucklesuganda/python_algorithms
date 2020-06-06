def linear_search(array, key):
    for i in range(len(array)):
        if array[i] == key:
            return i
    return -1
    

# n - length of array
# O(n) - linear search


def binary_search(array, key):
    if sorted(array) != array:
        raise ValueError("Array must be sorted")

    start = 0
    end = len(array)

    while start <= end:
        center = (start + end) // 2

        if array[center] == key:
            return center
        elif array[center] > key:
            end = center - 1
        elif array[center] < key:
            start = center + 1
    return -1


# O(log(n)) - binary search
arr = [0, 3, 1, -10, 200]
print(binary_search(sorted(arr), 5))

