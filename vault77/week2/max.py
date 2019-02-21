a = input('a: ')
a = int(a)
b = input('b: ')
b = int(b)

def max(a, b):
    if a > b:
        return a
    else:
        return b

print(max(a, b))