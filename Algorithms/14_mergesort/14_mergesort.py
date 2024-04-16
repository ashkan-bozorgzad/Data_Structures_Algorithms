def merge_sort(array):
    if len(array) <= 1:
        return None
    mid = len(array) // 2
    left = array[:mid]
    right = array[mid:]
    merge_sort(left)
    merge_sort(right)
    merge(array, left, right)


def merge(array, left, right):
    l_left = len(left)
    l_right = len(right)

    i = j = k = 0

    while i < l_left and j < l_right:
        if left[i] <= right[j]:
            array[k] = left[i]
            i += 1
        else:
            array[k] = right[j]
            j += 1
        k += 1

    while i < l_left:
        array[k] = left[i]
        k += 1
        i += 1

    while j < l_right:
        array[k] = right[j]
        k += 1
        j += 1


if __name__ == "__main__":
    test_cases = [
        [10, 3, 15, 7, 8, 23, 98, 29],
        [],
        [3],
        [9, 8, 7, 2],
        [1, 2, 3, 4, 5]
    ]

    for arr in test_cases:
        merge_sort(arr)
        print(arr)