lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def binary_search(lst, el):
    first = 0
    last = len(lst)
    found = False
    while first <= last and not found:
        middle = (first + last) // 2
        print(first, middle, last)
        if el < lst[middle]:
            last = middle - 1
        elif el > lst[middle]:
            first = middle + 1
        else:
            found = True
    return found

print(binary_search(lst, 9))