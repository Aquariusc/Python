def trim(s):
	n=0
	m=-1
	while s[n]==' ':
		n=n+1
	while s[m]==' ':
		m=m-1
	return s[n:len(s)+m+1]
print(trim(' hello world '))

'''
#递归
def trim(s):
	if len(s)==0:
		return s
	elif s[0]=='':
		return trim(s[1:])
	elif s[-1]=='':
		return trim(s[:-1])
	else:
		return s
print(trim('    '))
'''