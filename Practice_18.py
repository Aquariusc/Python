def createCounter():
	fn=0
	def counter():
		nonlocal fn
		fn=fn+1
		return fn
	return counter
counterA=createCounter()
print(counterA(),counterA())