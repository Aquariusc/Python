fpath=r'E:\Lucifer\Python\Test.txt'

with open(fpath,'r') as f:
	s=f.read()
	print(s)
'''
with open(fpath,'r') as f:
	s=f.readlines()
with open(fpath,'w') as w:
	for i in s:
		w.write(i.replace('Hello','Hi'))
'''