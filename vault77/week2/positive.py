numbers = [10, -1, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, -6]


def positive(numbers):
    result = []
    for num in numbers:
        if num >= 0:
            result.append(num)
    return result

print(positive(numbers))