
import unittest
from ..Maps import HashMap

def make_HashMap():
	x = HashMap()
	x["a"] = 1.11
	x["b"] = 2.22
	x["c"] = 3.33
	return x

class TestHashMap(unittest.TestCase):

	def test_getitem(self):
		x = make_HashMap()
		self.assertEquals(x["a"], 1.11)
		self.assertEquals(x["b"], 2.22)
		self.assertEquals(x["c"], 3.33)

	def test_len(self):
		x = make_HashMap()
		self.assertEquals(len(x), 3)

	def test_delitem(self):
		x = make_HashMap()
		del x["b"]
		with self.assertRaises(KeyError):
			x["b"]

	def test_items(self):
		x = make_HashMap()
		y = {("a", 1.11), ("b", 2.22), ("c", 3.33)}
		self.assertEquals(set(xi for xi in x.items()), y)

	def test_contains(self):
		x = make_HashMap()
		self.assertTrue("b" in x)
		self.assertFalse("z" in x)
