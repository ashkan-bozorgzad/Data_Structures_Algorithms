def shell_sort(array):
    size = len(array)
    gap = size // 2

    while gap > 0:
        for i in range(gap, size):
            key = array[i]
            j = i
            while j >= gap and array[j - gap] > key:
                array[j] = array[j - gap]
                j -= gap
            array[j] = key
        gap = gap // 2

    return array


if __name__ == '__main__':
    tests = [
        [89, 78, 61, 53, 23, 21, 17, 12, 9, 7, 6, 2, 1],
        [],
        [1, 5, 8, 9],
        [234, 3, 1, 56, 34, 12, 9, 12, 1300],
        [5]
    ]

    for elements in tests:
        shell_sort(elements)
        print(elements)
