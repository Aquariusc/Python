def findMinandMax(L):
	a=L[0]
	b=L[0]
	for i in L:
		if i>a:
			a=i
	for i in L:
		if i<b:
			b=i
	return (b,a)
print(findMinandMax([3,5,11,7,2,31,14]))