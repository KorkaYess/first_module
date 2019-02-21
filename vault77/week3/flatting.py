lst = [
    [
        [1, [2]],
        [3, [4, 5]]
    ],
    [6, 7]
]

def flatten(lst):
    result = []
    for item in lst:
        if type(item) == type([]):
            result.extend(flatten(item))
        else:
            result.append(item)

    return result


print(flatten(lst))