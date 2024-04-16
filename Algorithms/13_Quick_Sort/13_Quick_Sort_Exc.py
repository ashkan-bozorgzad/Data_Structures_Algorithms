def quick_sort(array, start, end):
    # If the array has only one element, it is already sorted.
    if start >= end:
        return None
    if start < end:
        pi = partition(array, start, end)
        # Recursively sort the sub-arrays.
        quick_sort(array, start, pi - 1)
        quick_sort(array, pi + 1, end)


def partition(array, start, end):
    pivot = end  # Choose the first element as the pivot.
    p_index = start

    for i in range(start, end):
        if array[i] <= array[pivot]:
            array[p_index], array[i] = array[i], array[p_index]
            p_index += 1

    array[p_index], array[pivot] = array[pivot], array[p_index]

    return p_index


if __name__ == '__main__':
    # elements = [11, 9, 29, 7, 2, 15, 28]
    elements = ["mona", "dhaval", "aamir", "tina", "chang"]
    quick_sort(elements, 0, len(elements) - 1)
    print(elements)

    tests = [
        [11, 9, 29, 7, 2, 15, 28],
        [3, 7, 9, 11],
        [25, 22, 21, 10],
        [29, 15, 28],
        [],
        [6]
    ]

    for elements in tests:
        quick_sort(elements, 0, len(elements) - 1)
        print(f'sorted array: {elements}')
