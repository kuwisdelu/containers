
class Node:

	def __init__(self, data = None, next = None):
		self.data = data
		self.next = next

	def __str__(self):
		if self.next is None:
			return f"Node({self.data})"
		else:
			return f"Node({self.data}) -> {self.next}"

	def __repr__(self):
		return str(self)

class BinaryNode:

	def __init__(self, key = None, value = None):
		self.key = key
		self.value = value
		self._parent = None
		self._left = None
		self._right = None

	def __str__(self):
		if self.left is None:
			left = None
		else:
			left = self.left.key
		if self.right is None:
			right = None
		else:
			right = self.right.key
		return str(left) + " <-{ " + str(self.key) + " }-> " + str(right)

	def __repr__(self):
		return str(self)

	@property
	def left(self):
		return self._left

	@left.setter
	def left(self, node):
		if node is not None:
			assert isinstance(node, BinaryNode)
			node._parent = self
		if self._left is not None:
			self._left._parent = None
		self._left = node

	@left.deleter
	def left(self):
		if self._left is not None:
			self._left._parent = None
		self._left = None

	@property
	def right(self):
		return self._right

	@right.setter
	def right(self, node):
		if node is not None:
			assert isinstance(node, BinaryNode)
			node._parent = self
		if self._right is not None:
			self._right._parent = None
		self._right = node

	@right.deleter
	def right(self):
		if self._right is not None:
			self._right._parent = None
		self._right = None

	@property
	def parent(self):
		return self._parent

