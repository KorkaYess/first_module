numbers = [10, 9, 11, 4, 12, 7, 13, 6, 14, 5, 15, 4, 16]

def min(numbers):
    minimum = numbers[0]
    mini = []

    for i in numbers:
        if i < minimum:
            minimum = i

    mini.append(minimum)
    numbers.remove(minimum)
    mini.extend(numbers)
    return mini
    
print(min(numbers))