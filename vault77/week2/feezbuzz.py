n = input('n: ')
n = int(n)

def fizzbuzz(n):
    i = 1
    while i <= n:
        if i % 2 == 0 and i % 3 == 0:
                print('fizzbuzz')
                i = i + 1
        else:
            if i % 2 == 0:
                print('fizz')
                i = i + 1

            if i % 3 == 0:
                print('buzz')
                i = i + 1
        
            else:
                print(i)
                i = i + 1

fizzbuzz(n)