'''def is_palindrome(n):
	if n<10:
		return n
	else:
		a=len(str(n))//2
		b=0
		c=-1
		for i in range(a):
			if str(n)[b]==str(n)[c]:
				b=b+1
				c=c-1
			else:
				return
		return n	'''

def is_palindrome(n):
    return str(n) == str(n)[::-1]
output=filter(is_palindrome,range(1,1000))
print('1~1000:',list(output))