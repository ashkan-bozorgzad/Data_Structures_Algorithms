def merge_sort(array, key=None, descending=False):
    if len(array) <= 1:
        return None
    key = key
    descending = descending
    mid = len(array) // 2
    left = array[:mid]
    right = array[mid:]
    merge_sort(left, key, descending)
    merge_sort(right, key, descending)
    merge(array, left, right, key, descending)


def merge(array, left, right, key=None, descending=False):
    l_left = len(left)
    l_right = len(right)

    i = j = k = 0

    while i < l_left and j < l_right:

        if descending:
            if left[i][key] >= right[j][key]:
                array[k] = left[i]
                i += 1
            else:
                array[k] = right[j]
                j += 1
            k += 1
        else:
            if left[i][key] <= right[j][key]:
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
    elements = [
        {'name': 'vedanth', 'age': 17, 'time_hours': 1},
        {'name': 'rajab', 'age': 12, 'time_hours': 3},
        {'name': 'vignesh', 'age': 21, 'time_hours': 2.5},
        {'name': 'chinmay', 'age': 24, 'time_hours': 1.5},
    ]

    merge_sort(elements, key='time_hours', descending=True)
    print(elements)

    merge_sort(elements, key='name')
    print(elements)