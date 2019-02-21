numbers = [8, 2, 3, 4, 5, 6, 7, 8, 9, 22]

def change(numbers):
    last_number = numbers[0]
    numbers[0] = numbers[-1]
    numbers[-1] = last_number
    return numbers 

print(change(numbers))   