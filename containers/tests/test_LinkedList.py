
import unittest
from ..Sequences import LinkedList

def make_LinkedList():
	x = LinkedList()
	x.append(1.11)
	x.append(2.22)
	x.append(3.33)
	return x

class TestLList(unittest.TestCase):

	def test_getitem(self):
		x = make_LinkedList()
		self.assertEquals(x[0], 1.11)
		self.assertEquals(x[1], 2.22)
		self.assertEquals(x[2], 3.33)

	def test_iter(self):
		x = make_LinkedList()
		self.assertEquals([xi for xi in x], [1.11, 2.22, 3.33])

	def test_len(self):
		x = make_LinkedList()
		self.assertEquals(len(x), 3)

	def test_delitem(self):
		x = make_LinkedList()
		del x[1]
		self.assertEquals(len(x), 2)
		self.assertEquals(x[0], 1.11)
		self.assertEquals(x[1], 3.33)

	def test_contains(self):
		x = make_LinkedList()
		self.assertTrue(2.22 in x)
