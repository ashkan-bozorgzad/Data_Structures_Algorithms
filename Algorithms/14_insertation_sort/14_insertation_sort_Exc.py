def median_sequence(array):
    for i in range (0, len(array)):
        key = array[i]
        j = i - 1
        while j >= 0 and array[j] > key:
            array[j + 1] = array[j]
            j-= 1
        array[j + 1] = key
        mid = i // 2
        if i % 2 == 0:
            print(array[mid])
        else:
            print((array[mid] + array[mid + 1]) / 2.0)


if __name__ == '__main__':
    element = [2, 1, 5, 7, 2, 0, 5]
    median_sequence(element)