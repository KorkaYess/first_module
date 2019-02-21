numbers = [1, 25, 3, 4, 25, 6, 7, 8, 9, 10, 11, 12]

def even(numbers):
    result = []
    for num in numbers:
        if num % 2 == 0:
            result.append(num)
    return result

def max(numbers):
    result = numbers[0]
    for num in numbers:
        if num > result:
            result = num
    return result

print(max(numbers))