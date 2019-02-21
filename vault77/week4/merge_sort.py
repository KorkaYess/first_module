def merge(left, right, lst):
    i = 0
    j = 0
    k = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            lst[k] = left[i]
            i = i + 1
        else:
            lst[k] = right[j]
            j = j + 1

        k = k + 1

    while i < len(left):
        lst[k] = left[i]
        i = i + 1
        k = k + 1

    while j < len(right):
        lst[k] = right[j]
        j = j + 1
        k = k + 1


def merge_sort(lst):
    if len(lst) < 2:
        return lst

    mid = len(lst) // 2
    left = lst[:mid]
    right = lst[mid:]

    merge_sort(left)
    merge_sort(right)

    merge(left, right, lst)


if __name__ == 'main':
    lst = [10, 8, 9, 15, 7, 6, 5, 2, 3]
    merge_sort(lst)
    print(lst)
    assert lst == [2, 3, 5, 6, 7, 8, 9, 10, 15]