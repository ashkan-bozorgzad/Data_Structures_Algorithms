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
    pivot = start  # Choose the first element as the pivot.
    left = start + 1
    right = end

    while left <= right:
        # Find the first element that is greater than the pivot.
        while left <= end and array[pivot] >= array[left]:
            left += 1
        # Find the first element that is less than the pivot.
        while array[pivot] <= array[right] and right > start:
            right -= 1

        if left > right:  # If the pointers have crossed, swap the pivot with the element at the right pointer.
            array[pivot], array[right] = array[right], array[pivot]
        else:  # Otherwise, swap the elements at the left and right pointers.
            array[left], array[right] = array[right], array[left]

    return right


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
