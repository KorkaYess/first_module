def sum(a, b):
	return a + b

def minus(a, b):
	return a - b

def sqare(a):
	return a*a

def calc(a, b, f):
	print('The result is: ' + str(f(a, b)))

calc(5, 4, sum)
calc(5, 4, minus)
sqare(5)