def bubble_sort(arr):
    size = len(arr)

    for i in range(size-1):
        swapped = False
        for j in range(size-1-i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break


if __name__ == '__main__':
    elements_1 = [1, 2, 3, 4, 2]
    elements_2 = ["mona", "dhaval", "aamir", "tina", "chang"]
    elements_3 = [5, 9, 2, 1, 67, 34, 88, 34]

    bubble_sort(elements_1)
    print(elements_1)

    bubble_sort(elements_2)
    print(elements_2)

    bubble_sort(elements_3)
    print(elements_3)
