
n = input('n: ')
n = int(n)

def fib(n):
    f1 = 1
    f2 = 1
    i = 1
    while i <= n:
        if i > 2:
            r = f1 + f2
            f1 = f2
            f2 = r
        else:
            r = 1
        i = i + 1
    return r

a = 1
while a <= n:
    print(fib(a))
    a = a + 1