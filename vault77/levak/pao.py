a = input('a: ')
a = int(a)
b = input('b: ')
b = int(b)
math = input('Opeaziya(+ - * /): ')

if math != '+' and math != '/' and math != '-' and math != '*':
    math = input('Neizvestaya operatsiya( + - * / ): ')
if math == '+':
    print(a + b)
if math == '-':
    print(a - b)
if math == '*':
    print(a * b)
if math == '/':
    print(a / b)