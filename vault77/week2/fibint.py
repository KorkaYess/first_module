
n = input('n: ')
n = int(n)

def fib(n):
        phi = ((5**0.5 + 1) / 2)
        return int(phi**n / 5**0.5 + 0.5)

a = 1
while a <= n:
    print(fib(a))
    a = a + 1