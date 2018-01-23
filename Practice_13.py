#失败
def triangles(max):
	L=[1]
	while True:
		yield L
		L=[*L,0,0]
		L=[L[i-1]+L[i] for i in range(len(L)-1)]