
from ..bstree import BSTree

import unittest

def test_BSTree_instance():
	x = BSTree()
	x.insert(12, "twelve")
	x.insert(5, "five")
	x.insert(18, "eighteen")
	x.insert(2, "two")
	x.insert(9, "nine")
	x.insert(15, "fifteen")
	x.insert(19, "nineteen")
	x.insert(17, "seventeen")
	return x

class TestLList(unittest.TestCase):

	def test_inorder(self):
		x = test_BSTree_instance()
		y = [2, 5, 9, 12, 15, 17, 18, 19]
		self.assertEquals(x.inorder(), y)

	def test_getitem(self):
		x = test_BSTree_instance()
		self.assertEquals(x[17], "seventeen")

	def test_insert(self):
		x = test_BSTree_instance()
		x.insert(13, "thirteen")
		self.assertEquals(x[13], "thirteen")

	def test_delete(self):
		x = test_BSTree_instance()
		x.delete(17)
		self.assertIs(x.search(17), None)

	def test_height(self):
		x = test_BSTree_instance()
		self.assertEquals(x.height(), 4)

	def test_contains(self):
		x = test_BSTree_instance()
		self.assertTrue(17 in x)
		self.assertFalse(13 in x)
