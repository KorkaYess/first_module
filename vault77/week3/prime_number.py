number = input('Choose a number: ' )
number = int(number)

def is_prime(number):
    result = True 
    for i in range(2, number):
        if number % i == 0:
            result = False
    return result

is_prime(number)
if is_prime(number):
    print('Prime')
else:
    print('Not prime')

assert is_prime(2)
assert is_prime(3)
assert is_prime(5)
assert is_prime(7)
assert is_prime(97)
assert not is_prime(93)
assert not is_prime(4)
assert is_prime(11)
assert not is_prime(12)
assert is_prime(13)