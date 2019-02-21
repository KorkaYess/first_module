n = input('n: ')
n = int(n)

def fizzbuzz(n):
    for i in range(1, m + 1):

        if i % 2 == 0 and i % 3 == 0:
            print('fizzbuzz')

        elif i % 2 == 0:
            print('fizz')

        elif i % 3 == 0:
            print('buzz')

        else:
            print(i)

fizzbuzz(n)