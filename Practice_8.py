def product(*x):
	s=1
	for a in x:
		s=s*a
	return s
print(product(5,6,7,9))