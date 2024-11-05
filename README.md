
# Example data structures for DS 5010

Reference implementations of standard data structures

## Package organization

The package is organized into two subpackages:

- `Sequences` for sequential (indexable) containers
- `Maps` for associative (key-value) containers

### Sequential containers

The `Sequences` subpackage provides the following classes in respectively-named modules:

- `LinkedList`: singly-linked list
- `Vector`: A generic vector, with specializations:
	+ `NumericVector`: Array-backed numeric vector with support for arithmetic operators
	+ `IntegerVector`
	+ `DoubleVector`

### Associative containers

The `Maps` subpackage provides the following classes in respectively-named modules:

- `HashMap`: A closed address hash table
- `TreeMap`: A binary search tree

### Importing

For convenience, the following classes can be imported directly from the top-level `containers` package (rather than importing from subpackages):

- `LinkedList`
- `IntegerVector`
- `DoubleVector`
- `HashMap`
- `TreeMap`

## Example usage

The classes in this package behave similarly to Python's built-in `list` and `dict` types.

### Linked lists

We can create a linked list by importing the `LinkedList` class and initializing it from a `list`:

```
from containers import LinkedList

ll = LinkedList([1.11, 2.22, 3.33])
print(ll)
```

Alternatively, we can build up the list item by item:

```
ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
print(ll)

ll.extend([4,5,6])
print(ll)
```

### Vectors

The provided `Vector` class simply wraps Python's built-in `list` type. However, the subclasses `IntegerVector` and `DoubleVector` use a static array to support fast, vectorized arithmetic operations similar to `numpy`.

For integers:

```
from containers import IntegerVector

vi = IntegerVector([100, 200, 300])
print(vi)
print(vi + 10)
print(vi + vi)
```

For doubles:

```
from containers import DoubleVector

vd = DoubleVector([1.11, 2.22, 3.33])
print(vd)
print(vd + 10)
print(vd + vd)
```

### Hash maps

We can create a hash map by importing a `HashMap` and initializing it from a `dict`:

```
from containers import HashMap

hm = HashMap({"a": 1, "b": 2, "c": 3})
print(hm)

hm["d"] = 100
print(hm)
```

Note that the `HashMap` class does not guarantee ordering of its key-value pairs.

Also, it uses closed addressing, so key collisions are resolved by chaining.

### Binary searc tree

We can create a binary search tree by importing a `TreeMap` and initializing it from a `dict`:

```
from containers import TreeMap

tm = TreeMap({1: "one", 2: "two", 3: "three"})
print(tm)

tm[4] = "four"
print(tm)
```

Note that the `TreeMap` class is not self balancing when setting or deleting individual key-value pairs. It will, however, update itself in a balanced way when provided with an iterable:

```
tm = TreeMap()
tm.update({1: "one", 2: "two", 3: "three",
	5: "five", 6: "six", 7: "seven"})
print(tm.root)
print(tm.root.left)
print(tm.root.right)
```
