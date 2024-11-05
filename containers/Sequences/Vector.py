
import math
from array import array

class Vector:
	"""
	A generic vector supporting random access
	"""

	def __init__(self, data):
		"""
		Initialize a Vector from an iterable
		"""
		if isinstance(data, Vector):
			self._data = data.data[:]
		else:
			self._data = list(data)

	def __str__(self):
		"""
		Return str(self)
		"""
		s = ",".join([str(x) for x in self.data])
		s = type(self).__name__ + "([" + s + ")]"
		return s

	def __repr__(self):
		"""
		Return repr(self)
		"""
		return str(self)

	def __len__(self):
		"""
		Return len(self)
		"""
		return len(self.data)

	def __iter__(self):
		"""
		Return iter(self)
		"""
		return iter(self.data)

	def __getitem__(self, i):
		"""
		Get self[i]
		"""
		if isinstance(i, slice):
			return type(self)(self.data[i])
		else:
			return self.data[i]

	def __setitem__(self, i, value):
		"""
		Set self[i] = value
		"""
		self.data[i] = value

	def sort(self):
		"""
		Sort the vector
		"""
		self.data = sorted(self.data)

	def reverse(self):
		"""
		Reverse the vector
		"""
		self.data = reversed(self.data)

	@property
	def data(self):
		return self._data

class NumericVector(Vector):
	"""
	A numeric vector supporting arithmetic
	"""

	def __init__(self, data, typecode = None):
		"""
		Initialize a NumericVector
		"""
		if isinstance(data, NumericVector):
			self._data = data.data[:]
		elif isinstance(data, array):
			self._data = data
		else:
			self._data = array(typecode, data)

	def __add__(self, y):
		"""
		Return self + y
		"""
		if isinstance(y, (int, float)):
			result = (xi + y for xi in self)
		else:
			result = (xi + yi for xi, yi in zip(self, y))
		return NumericVector(result, self.typecode)

	def __sub__(self, y):
		"""
		Return self - y
		"""
		if isinstance(y, (int, float)):
			result = (xi - y for xi in self)
		else:
			result = (xi - yi for xi, yi in zip(self, y))
		return NumericVector(result, self.typecode)

	def __mul__(self, y):
		"""
		Return self * y
		"""
		if isinstance(y, (int, float)):
			result = (xi * y for xi in self)
		else:
			result = (xi * yi for xi, yi in zip(self, y))
		return NumericVector(result, self.typecode)

	def __truediv__(self, y):
		"""
		Return self / y
		"""
		if isinstance(y, (int, float)):
			result = (xi / y for xi in self)
		else:
			result = (xi / yi for xi, yi in zip(self, y))
		return NumericVector(result, self.typecode)

	def __floordiv__(self, y):
		"""
		Return self // y
		"""
		if isinstance(y, (int, float)):
			result = (xi // y for xi in self)
		else:
			result = (xi // yi for xi, yi in zip(self, y))
		return NumericVector(result, self.typecode)

	def __mod__(self, y):
		"""
		Return self % y
		"""
		if isinstance(y, (int, float)):
			result = (xi % y for xi in self)
		else:
			result = (xi % yi for xi, yi in zip(self, y))
		return NumericVector(result, self.typecode)

	def __pow__(self, y):
		"""
		Return self ** y
		"""
		if isinstance(y, (int, float)):
			result = (xi ** y for xi in self)
		else:
			result = (xi ** yi for xi, yi in zip(self, y))
		return NumericVector(result, self.typecode)

	def dot(self, y):
		"""
		Return inner product of self and y
		"""
		prod = 0
		for xi, yi, in zip(self, y):
			prod += xi * yi
		return prod

	def norm1(self):
		"""
		Return L1 norm of self
		"""
		return sum([abs(x) for x in self.data])

	def norm2(self):
		"""
		Return L2 norm of self
		"""
		return math.sqrt(sum([x ** 2 for x in self.data]))

	@property
	def typecode(self):
		"""
		Get the typecode of the underlying array
		"""
		return self.data.typecode

	@property
	def data(self):
		"""
		Get the underlying array
		"""
		return self._data

	@data.setter
	def data(self, value):
		"""
		Set the underlying array
		"""
		self._data = array(self.typecode, value)

class IntegerVector(NumericVector):
	"""
	A vector of integers supporting arithmetic
	"""

	def __init__(self, data):
		"""
		Initialize an IntegerVector
		"""
		super().__init__(data, "l")

class DoubleVector(NumericVector):
	"""
	A vector of doubles supporting arithmetic
	"""

	def __init__(self, data):
		"""
		Initialize a DoubleVector
		"""
		super().__init__(data, "d")

