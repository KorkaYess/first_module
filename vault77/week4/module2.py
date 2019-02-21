from merge_sort import merge


lst = [10, 8, 4, 12, 13, 14, 5, 7, 6]
left = [4, 8, 10, 12, 13]
right = [5, 6, 7, 14]
merge(left, right, lst)
print(lst)