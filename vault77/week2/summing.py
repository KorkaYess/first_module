numbers1 = [1, 2, 3, 4]
numbers2 = [5, 6, 7, 8]

def add_list(numbers1, numbers2):
    Sum = []
    for i, j in zip(numbers1, numbers2):
        Sum.append(i + j)
    return Sum

print(add_list(numbers1, numbers2))