
from ..Nodes import BinaryNode

class TreeMap:

	def __init__(self, iterable = None):
		"""
		Initialize a TreeMap from an iterable
		"""
		if isinstance(iterable, BinaryNode):
			self._nitems = len(traverse_inorder(iterable))
			self._root = iterable
		else:
			self._nitems = 0
			self._root = None
			if iterable is not None:
				self.update(iterable)

	def __str__(self):
		"""
		Return str(self)
		"""
		items = self.inorder()
		s = ", ".join(f"{str(key)}: {str(val)}" for key, val in items)
		return f"TreeMap({{{s}}})"

	def __repr__(self):
		"""
		Return repr(self)
		"""
		return str(self)
	
	def __len__(self):
		"""
		Return len(self)
		"""
		return self._nitems
	
	def __iter__(self):
		"""
		Return iterator using self.inorder()
		"""
		return self.inorder()

	@property
	def root(self):
		"""
		Get the root node
		"""
		return self._root

	@root.setter
	def root(self, node):
		"""
		Set the root node
		"""
		if node is not None:
			assert isinstance(node, BinaryNode)
		self._root = node

	def search(self, key):
		"""
		Searches the tree for a node by key
		"""
		node = self.root
		while node is not None and key != node.key:
			if key < node.key:
				node = node.left
			else:
				node = node.right
		return node
	
	def __contains__(self, key):
		"""
		Return key in self
		"""
		return self.search(key) is not None

	def set(self, key, value):
		"""
		Set self[key] = value
		"""
		node = BinaryNode(key, value)
		parent = None
		current = self.root
		while current is not None:
			parent = current
			if node.key < current.key:
				current = current.left
			elif node.key > current.key:
				current = current.right
			else:
				current = None
		if parent is None:
			self.root = node
			self._nitems += 1
		elif node.key < parent.key:
			parent.left = node
			self._nitems += 1
		elif node.key > parent.key:
			parent.right = node
			self._nitems += 1
		else:
			parent.value = value

	def __setitem__(self, key, value):
		"""
		Set self[key] = value
		"""
		self.set(key, value)

	def get(self, key):
		"""
		Get self[key]
		"""
		return self.search(key).value

	def __getitem__(self, key):
		"""
		Get self[key]
		"""
		node = self.search(key)
		if node is None:
			raise KeyError
		else:
			return node.value

	def delete(self, key):
		"""
		Delete self[key]
		"""
		node = self.search(key)
		# key not found
		if node is None:
			return
		# no left child
		if node.left is None:
			self.transplant(node, node.right)
		# no right child
		elif node.right is None:
			self.transplant(node, node.left)
		else:
			# find successor (node with next largest key)
			successor = self.successor(node.key)
			# handle case if successor lies within a subtree
			if successor.parent is not node:
				# replace successor with its right child
				self.transplant(successor, successor.right)
				successor.right = node.right
			# transplant successor and update left child
			self.transplant(node, successor)
			successor.left = node.left
		self._nitems -= 1

	def __delitem__(self, key):
		return self.delete(key)

	def min(self):
		"""
		Get the node with the minimum key
		"""
		node = self.root
		while node.left is not None:
			node = node.left
		return node

	def max(self):
		"""
		Get the node with the maximum key
		"""
		node = self.root
		while node.right is not None:
			node = node.right
		return node

	def successor(self, key = None):
		"""
		Get the successor of a node by key (if it exists)
		"""
		if key is None:
			node = self.root
		else:
			node = self.search(key)
		if node.right is not None:
			return TreeMap(node.right).min()
		parent = node.parent
		while parent is not None and node is parent.right:
			node = parent
			parent = parent.parent
		return parent

	def predecessor(self, key = None):
		"""
		Get the predecessor of a node by key (if it exists)
		"""
		if key is None:
			node = self.root
		else:
			node = self.search(key)
		if node.left is not None:
			return TreeMap(node.left).max()
		parent = node.parent
		while parent is not None and node is parent.left:
			node = parent
			parent = parent.parent
		return parent

	def transplant(self, x, y):
		"""
		Replaces subtree rooted at node x with subtree rooted at node y
		"""
		if x.parent is None:
			self.root = y
		elif x is x.parent.left:
			x.parent.left = y
		else:
			x.parent.right = y

	def update(self, iterable):
		"""
		Update tree from an iterable in a balanced way
		"""
		if isinstance(iterable, dict):
			iterable = iterable.items()
		x = sorted(iterable)
		if len(x) > 0:
			mid = len(x) // 2
			self.set(*x[mid])
			self.update(x[:mid])
			self.update(x[mid+1:])

	def inorder(self):
		"""
		In-order iteration over (key, value) tuples
		"""
		stack = []
		node = self.root
		while len(stack) > 0 or node is not None:
			if node is not None:
				stack.append(node)
				node = node.left
			else:
				node = stack.pop(-1)
				yield (node.key, node.value)
				node = node.right

	def preorder(self):
		"""
		Pre-order traversal over (key, value) tuples
		"""
		stack = []
		stack.append(self.root)
		while len(stack) > 0:
			node = stack.pop(-1)
			if node is not None:
				yield (node.key, node.value)
				if node.right is not None:
					stack.append(node.right)
				if node.left is not None:
					stack.append(node.left)

	def levelorder(self):
		"""
		Level-order traversal over (key, value) tuples
		"""
		queue = []
		queue.append(self.root)
		while len(queue) > 0:
			node = queue.pop(0)
			yield (node.key, node.value)
			if node.left is not None:
				queue.append(node.left)
			if node.right is not None:
				queue.append(node.right)

	def height(self):
		"""
		Get the height of the tree
		"""
		height = 0
		queue = []
		queue.append(self.root)
		while len(queue) > 0:
			size = len(queue)
			# pop all nodes at current level and enqueue their children
			for n in range(size):
				node = queue.pop(0)
				if node.left is not None:
					queue.append(node.left)
				if node.right is not None:
					queue.append(node.right)
			height += 1
		return height

### Recursive versions of tree traversal/search

def traverse_inorder(node):
	"""
	In-order depth-first traversal (DFS) using recursion
	"""
	if node is None:
		return []
	else:
		left = traverse_inorder(node.left)
		right = traverse_inorder(node.right)
		return left + [(node.key, node.value)] + right

def traverse_preorder(node):
	"""
	Pre-order depth-first traversal (DFS) using recursion
	"""
	if node is None:
		return []
	else:
		left = traverse_preorder(node.left)
		right = traverse_preorder(node.right)
		return [(node.key, node.value)] + left + right

def traverse_level(node, level = 1):
	"""
	Level-order breadth-first-traversal (DFS) using recursion
	"""
	if node is None:
		return []
	elif level == 1:
		return [(node.key, node.value)]
	else:
		left = traverse_level(node.left, level - 1)
		right = traverse_level(node.right, level - 1)
		return left + right

def search_binary_tree(node, key):
	"""
	Search tree for a node by key using recursion
	"""
	if node is None or key == node.key:
		return node
	if key < node.key:
		return search_binary_tree(node.left, key)
	else:
		return search_binary_tree(node.right, key)

