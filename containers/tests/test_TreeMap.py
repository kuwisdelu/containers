
import unittest
from ..Maps import TreeMap

def make_TreeMap():
	x = TreeMap()
	x.set(12, "twelve")
	x.set(5, "five")
	x.set(18, "eighteen")
	x.set(2, "two")
	x.set(9, "nine")
	x.set(15, "fifteen")
	x.set(19, "nineteen")
	x.set(17, "seventeen")
	return x

class TestTreeMap(unittest.TestCase):

	def test_inorder(self):
		x = make_TreeMap()
		y = [
			(2, "two"),
			(5, "five"),
			(9, "nine"),
			(12, "twelve"),
			(15, "fifteen"),
			(17, "seventeen"),
			(18, "eighteen"),
			(19, "nineteen")]
		self.assertEquals(list(x.inorder()), y)

	def test_getitem(self):
		x = make_TreeMap()
		self.assertEquals(x[17], "seventeen")

	def test_set(self):
		x = make_TreeMap()
		x.set(13, "thirteen")
		self.assertEquals(x[13], "thirteen")

	def test_delete(self):
		x = make_TreeMap()
		x.delete(17)
		self.assertIs(x.search(17), None)

	def test_height(self):
		x = make_TreeMap()
		self.assertEquals(x.height(), 4)

	def test_contains(self):
		x = make_TreeMap()
		self.assertTrue(17 in x)
		self.assertFalse(13 in x)
