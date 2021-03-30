
from ..htable import HTable

import unittest

def test_HTable_instance():
	x = HTable()
	x["a"] = 1.11
	x["b"] = 2.22
	x["c"] = 3.33
	return x

class TestLList(unittest.TestCase):

	def test_getitem(self):
		x = test_HTable_instance()
		self.assertEquals(x["a"], 1.11)
		self.assertEquals(x["b"], 2.22)
		self.assertEquals(x["c"], 3.33)

	def test_len(self):
		x = test_HTable_instance()
		self.assertEquals(len(x), 3)

	def test_delitem(self):
		x = test_HTable_instance()
		del x["b"]
		with self.assertRaises(KeyError):
			x.get("b")

	def test_items(self):
		x = test_HTable_instance()
		y = {("a", 1.11), ("b", 2.22), ("c", 3.33)}
		self.assertEquals(set(xi for xi in x.items()), y)

	def test_contains(self):
		x = test_HTable_instance()
		self.assertTrue("b" in x)
		self.assertFalse("z" in x)
