def fac(number):
    if number == 1:
        return 1
    return number * fac(number - 1)

result = fac(7)
print(result)