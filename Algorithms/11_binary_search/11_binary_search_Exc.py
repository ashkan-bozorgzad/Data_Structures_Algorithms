def linear_search(arr, target):
    all_index = []
    for index, val in enumerate(arr):
        if val == target:
            all_index.append(index)
    return all_index if all_index else -1


def Linear_search_1(arr, target):
    all_index = []
    for i in range(len(arr)):
        if arr[i] == target:
            all_index.append(i)
    return all_index if all_index else -1


def binary_search(arr, target):
    left_index = 0
    right_index = len(arr) - 1
    all_index = []

    while left_index <= right_index:
        mid_index = (left_index + right_index) // 2
        mid_val = arr[mid_index]

        if target == mid_val:
            all_index.append(mid_index)

            step = 1
            while target == arr[mid_index + step]:
                all_index.append(mid_index + step)
                step += 1

            step = 1
            while target == arr[mid_index - step]:
                all_index.append(mid_index - step)
                step += 1

            return all_index

        if target < mid_val:
            right_index = mid_index -1

        elif target > mid_val:
            left_index = mid_index + 1

    return  -1


def binary_search_recursive(arr, target, left_index, right_index):
    all_index = []

    if right_index < left_index:
        return -1

    mid_index = (left_index + right_index) // 2
    mid_val = arr[mid_index]

    if mid_index >= len(arr) or mid_index < 0:
        return -1

    if mid_val == target:
        all_index.append(mid_index)

        step = 1
        while target == arr[mid_index + step]:
            all_index.append(mid_index + step)
            step += 1

        step = 1
        while target == arr[mid_index - step]:
            all_index.append(mid_index - step)
            step += 1

        return all_index

    elif target < mid_val:
        right_index = mid_index - 1
    else:
        left_index = mid_index + 1

    return binary_search_recursive(arr, target, left_index, right_index)


if __name__ == '__main__':
    numbers_list = [1,4,6,9,11,15,15,15,17,21,34,34,56]
    target = 15


    index_1 = linear_search(numbers_list, target)
    print(f"Number found at index {index_1} using linear search")

    index_2 = Linear_search_1(numbers_list, target)
    print(f"Number found at index {index_2} using linear search")

    index_3 = binary_search(numbers_list, target)
    print(f"Number found at index {index_3} using binary search")

    index_4 = binary_search_recursive(numbers_list, target, 0, len(numbers_list) - 1)
    print(f"Number found at index {index_3} using binary search")







