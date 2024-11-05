
from ..Nodes import Node

class LinkedList:

	def __init__(self, iterable = None):
		"""
		Initialize a LinkedList from an iterable
		"""
		self.head = None
		if iterable is not None:
			self.extend(iterable)

	def __str__(self):
		"""
		Return str(self)
		"""
		s = ", ".join((str(s) for s in self))
		return f"LinkedList([{s}])"

	def __repr__(self):
		"""
		Return repr(self)
		"""
		return str(self)

	def __len__(self):
		"""
		Return len(self)
		"""
		size = 0
		for i in self:
			size += 1
		return size

	def __iter__(self):
		"""
		Return iter(self)
		"""
		node = self.head
		while node is not None:
			yield node.data
			node = node.next

	def append(self, val):
		"""
		Append item to the list
		"""
		node = Node(val)
		if self.head is None:
			self.head = node
		else:
			tail = self.head
			while tail.next is not None:
				tail = tail.next
			tail.next = node

	def extend(self, iterable):
		"""
		Extend the list with an iterable
		"""
		tail = self.head
		for val in iterable:
			node = Node(val)
			if self.head is None:
				self.head = node
				tail = node
			else:
				while tail.next is not None:
					tail = tail.next
				tail.next = node
				tail = tail.next

	def get(self, i):
		"""
		Get self[i]
		"""
		node = self.head
		cur = 0
		while node is not None:
			if cur == i:
				return node.data
			else:
				node = node.next
				cur += 1
		raise IndexError

	def __getitem__(self, i):
		"""
		Get self[i]
		"""
		return self.get(i)

	def insert(self, i, val):
		"""
		Insert item at self[i]
		"""
		before = None
		after = self.head
		if i == 0:
			if after is None:
				self.head = Node(val, None)
			else:
				self.head = Node(val, after)
		else:
			cur = 0
			while after is not None:
				if cur == i:
					break
				before = after
				after = after.next
				cur += 1
			if after is None:
				if cur == i - 1:
					before.next = Node(val, None)
				else:
					raise IndexError
			else:
				before.next = Node(val, after)

	def delete(self, i):
		"""
		Delete self[i]
		"""
		node = self.head
		cur = 0
		if i == 0:
			if node is None:
				raise IndexError
			else:
				self.head = node.next
		else:
			while node is not None:
				if cur == i:
					break
				prev = node
				node = node.next
				cur += 1
			if node is None:
				raise IndexError
			else:
				prev.next = node.next

	def __delitem__(self, i):
		"""
		Delete self[i]
		"""
		self.delete(i)

	def push(self, val):
		"""
		Prepend a new item
		"""
		if self.head is None:
			self.head = Node(val)
		else:
			self.head = Node(val, self.head)

	def pop(self):
		"""
		Remove and return the first item
		"""
		if self.head is None:
			raise IndexError("list is empty")
		else:
			node = self.head
			self.head = node.next
			return node.data

	def peek(self):
		"""
		Return the first item
		"""
		if self.head is None:
			raise IndexError("list is empty")
		else:
			return self.head.data

	def map(self, fun, **kwargs):
		"""
		Apply a function to every item
		"""
		node = self.head
		while node is not None:
			node.data = fun(node.data, **kwargs)
			node = node.next

