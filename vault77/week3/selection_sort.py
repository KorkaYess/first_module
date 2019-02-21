numbers = [10, 15, 3, 6, 7, 1, 3, 9, 12]

def min(numbers):
    min = numbers[0]
    for number in numbers:
        if number < min:
            min = number
    return min

def move(numbers, idx):
    return [numbers[idx]] + numbers[:idx] + numbers[idx + 1:]

def selection_sort(numbers):
    for i in range(len(numbers)):
        sorted_numbers = numbers[:i]
        unsorted_numbers = numbers[i:]
        min_number = min(unsorted_numbers)
        numbers = sorted_numbers + move(unsorted_numbers, unsorted_numbers.index(min_number))
    return numbers

assert selection_sort([10, 15, 3, 6, 7, 1, 3, 9, 12]) == [1, 3, 3, 6, 7, 9, 10, 12, 15]
assert selection_sort([10, 15, 3, 6, 7, 3, 9, 12]) == [3, 3, 6, 7, 9, 10, 12, 15]
assert selection_sort([10, 15, 3, 6, 7, 9, 12]) == [3, 6, 7, 9, 10, 12, 15]
assert selection_sort([10, 15, 7, 9, 12]) == [7, 9, 10, 12, 15]
assert selection_sort([10, 15, 9, 12]) == [9, 10, 12, 15]

print(selection_sort(numbers))