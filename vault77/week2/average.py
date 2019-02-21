numbers = [10, 9, 11, 8, 12, 1, 14, 6, 14, 5]

def average(numbers):
    a = 0
    for i in numbers:
        a = a + i
    print('The sum is: ' + str(a))
    average = a / len(numbers)
    return average

print('The average is: ' + str(average(numbers)))