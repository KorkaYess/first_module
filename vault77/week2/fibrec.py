
n = input('n: ')
n = int(n)

def fib(n):
    if n > 2:
    	return fib(n - 1) + fib(n - 2)
    return 1

a = 1
while a <= n:
    print(fib(a))
    a = a + 1