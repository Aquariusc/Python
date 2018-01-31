import unittest

from Practice_26 import Student

class TestStudent(unittest.TestCase):
	def test_0_to_60(self):
		s1=Student('Jason',0)
		s2=Student('Lucifer',59)
		self.assertEqual(s1.get_grade(),'C')
		self.assertEqual(s2.get_grade(),'C')

	def test_60_to_80(self):
		s1=Student('Jason',60)
		s2=Student('Lucifer',79)
		self.assertEqual(s1.get_grade(),'B')
		self.assertEqual(s2.get_grade(),'B')

	def test_80_to_100(self):
		s1=Student('Jason',80)
		s2=Student('Lucifer',100)
		self.assertEqual(s1.get_grade(),'A')
		self.assertEqual(s2.get_grade(),'A')

	def test_invalid(self):
		s1=Student('Jason',-1)
		s2=Student('Lucifer',101)
		with self.assertRaises(ValueError):
			s1.get_grade()
		with self.assertRaises(ValueError):
			s2.get_grade()

if __name__=='__main__':
	unittest.main()