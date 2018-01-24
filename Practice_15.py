from functools import reduce
def prod(L):
	def Product(x,y):
		return x*y
	return reduce(Product,L)
print('3*5*7*9=',prod([3,5,7,9]))