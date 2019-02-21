numbers1 = [1, 3, 5, 7, 9, 11]
numbers2 = [7, 5, 6, 8, 1]

def add_list(numbers1, numbers2):
    result = []
    
    if len(numbers1) > len(numbers2):
        while len(numbers1) != len(numbers2):
            numbers2.append(0)
    else:
        while len(numbers1) != len(numbers2):
            numbers1.append(0)

    for i in range(len(numbers1)):
        result.append(numbers1[i] + numbers2[i])

    return result

print(add_list(numbers1, numbers2))