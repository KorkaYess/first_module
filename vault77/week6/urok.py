class RationalNumber:
	def __init__(self, num, denum):
		self.num = num
		self.denum = denum

	@staticmethod
	def add_static(a, b):
		returrn a + b

	def add(self, rational):
		# 1/2 +2/3 = 3/6 + 4/6 = 7/6
		result_denum = self.denum * rational.denum
		result_num = self.num * result_denum / self.denum + \
			rational.num * result_denum / rational.denum
		result = RationalNumber(int(result_num), result_denum)
		return result

	def __add__(self, retional):
		return self.add(rational)

	def __repr__(self):
		return '{}/{}'.format(self.num, self.denum)

if __name__ == '__main__':
	a = Rational(1/2)
	b = Rational(2/3)
	# try:
		# print(a + 1)
	# except()
	