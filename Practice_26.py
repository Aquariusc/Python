import unittest

class Student(object):
	def __init__(self,name,score):
		self.name=name
		self.score=score
	def get_grade(self):
		if 80>self.score>=60:
			return 'B'
		if 100>=self.score>=80:
			return 'A'
		if 60>self.score>=0:
			return 'C'
		else:
			raise ValueError