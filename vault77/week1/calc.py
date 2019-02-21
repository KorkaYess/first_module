is_number = False
while not is_number:
    a = input('a: ')
    try:
        a = int(a)
        is_number = True
    except ValueError:
        print('"{}" is not a number. Try again.'.format(a))

is_number = False
while not is_number:
    b = input('b: ')
    try:
        b = int(b)
        is_number = True
    except ValueError:
        print('"{}" is not a number. Try again.'.format(b))

action = input('Action ( + - * / ) ')
if action == '+':
    result = a + b
if action == '-':
    result = a - b
if action == '*':
    result = a * b
if action == '/':
    result = a / b

print('Your answer is: ' + str(result))

