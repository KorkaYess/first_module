numbers = [10, 20, 30, 40, 5, 6, 7, 8, 9, 15]

def reverse_list(numbers):
    reversed_list = []
    for i in range(len(numbers)):
        reversed_list.append(numbers[- i - 1])

    return reversed_list

print(reverse_list(numbers))