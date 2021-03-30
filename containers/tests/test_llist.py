
from ..llist import LList

import unittest

def test_LList_instance():
	x = LList()
	x.append(1.11)
	x.append(2.22)
	x.append(3.33)
	return x

class TestLList(unittest.TestCase):

	def test_getitem(self):
		x = test_LList_instance()
		self.assertEquals(x[0], 1.11)
		self.assertEquals(x[1], 2.22)
		self.assertEquals(x[2], 3.33)

	def test_iter(self):
		x = test_LList_instance()
		self.assertEquals([xi for xi in x], [1.11, 2.22, 3.33])

	def test_len(self):
		x = test_LList_instance()
		self.assertEquals(len(x), 3)

	def test_delitem(self):
		x = test_LList_instance()
		del x[1]
		self.assertEquals(len(x), 2)
		self.assertEquals(x[0], 1.11)
		self.assertEquals(x[1], 3.33)

	def test_insert(self):
		x = test_LList_instance()
		x.insert(1, 99)
		self.assertEquals(len(x), 4)
		self.assertEquals(x[0], 1.11)
		self.assertEquals(x[1], 99)
		self.assertEquals(x[2], 2.22)

	def test_index(self):
		x = test_LList_instance()
		self.assertEquals(x.index(2.22), 1)

	def test_contains(self):
		x = test_LList_instance()
		self.assertTrue(2.22 in x)
