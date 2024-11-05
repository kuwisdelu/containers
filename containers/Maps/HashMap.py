
class HashMap:

	def __init__(self, iterable = None, buckets = 1000):
		"""
		Initialize a HashMap from an iterable
		"""
		self._nbuckets = buckets
		self._nitems = 0
		self._keys = [[] for i in range(buckets)]
		self._values = [[] for i in range(buckets)]
		if iterable is not None:
			if isinstance(iterable, dict):
				iterable = iterable.items()
			for key, val in iterable:
				self.set(key, val)

	def __str__(self):
		"""
		Return str(self)
		"""
		items = zip(self.keys(), self.values())
		s = ", ".join(f"{str(key)}: {str(val)}" for key, val in items)
		return f"HashMap({{{s}}})"

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
		Return iterator using self.items()
		"""
		return self.items()

	def hashkey(self, key):
		"""
		Get the bucket for a key by applying the hash functino
		"""
		return hash(key) % self._nbuckets

	def loadfactor(self):
		"""
		Get the current load factor
		"""
		return len(self) / self._nbuckets
	
	def search(self, key):
		"""
		Searches the hash map for a key-value pair
		"""
		bucket = self.hashkey(key)
		if key in self._keys[bucket]:
			i = self._keys[bucket].index(key)
			return (key, self._values[bucket][i])
		else:
			return None

	def set(self, key, value):
		"""
		Set self[key] = value
		"""
		bucket = self.hashkey(key)
		if key in self._keys[bucket]:
			i = self._keys[bucket].index(key)
			self._values[bucket][i] = value
		else:
			self._keys[bucket].append(key)
			self._values[bucket].append(value)
			self._nitems += 1

	def __setitem__(self, key, value):
		"""
		Set self[key] = value
		"""
		self.set(key, value)

	def get(self, key, default = None):
		"""
		Get self[key]
		"""
		bucket = self.hashkey(key)
		if key in self._keys[bucket]:
			i = self._keys[bucket].index(key)
			return self._values[bucket][i]
		else:
			return default

	def __getitem__(self, key):
		"""
		Get self[key]
		"""
		item = self.search(key)
		if item is None:
			raise KeyError
		else:
			key, value = item
			return value
	
	def __contains__(self, key):
		"""
		Get key in self
		"""
		bucket = self.hashkey(key)
		return key in self._keys[bucket]

	def delete(self, key):
		"""
		Delete self[key]
		"""
		bucket = self.hashkey(key)
		if key in self._keys[bucket]:
			i = self._keys[bucket].index(key)
			del self._keys[bucket][i]
			del self._values[bucket][i]
			self._nitems -= 1

	def __delitem__(self, key):
		"""
		Delete self[key]
		"""
		self.delete(key)

	def keys(self):
		"""
		Get generator sequence of keys
		"""
		for bucket in range(self._nbuckets):
			for key in self._keys[bucket]:
				yield key

	def values(self):
		"""
		Get generator sequence of values
		"""
		for bucket in range(self._nbuckets):
			for val in self._values[bucket]:
				yield val

	def items(self):
		"""
		Get generator for items as (key, value) tuples
		"""
		for bucket in range(self._nbuckets):
			for key, val in zip(self._keys[bucket], self._values[bucket]):
				yield (key, val)

