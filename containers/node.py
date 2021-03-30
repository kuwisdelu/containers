
### A node class for a singly-linked list

class LNode:

    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next

    def __str__(self):
        if self.getnext() is None:
            next_ = None
        else:
            next_ = self.getnext().getdata()
        return "{ " + str(self.getdata()) + " }-> " + str(next_)

    def __repr__(self):
        return str(self)

    def getdata(self):
        """Get the node's data payload."""
        return self.data

    def setdata(self, data = None):
        """Set the node's data payload."""
        self.data = data

    def getnext(self):
        """Get the next linked node."""
        return self.next

    def setnext(self, node = None):
        """Set the next linked node."""
        self.next = node


### A node for a tree-like data structure

class TNode:

    def __init__(self, key = None, value = None):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.parent = None

    def __str__(self):
        if self.getleft() is None:
            left = None
        else:
            left = self.getleft().getkey()
        if self.getright() is None:
            right = None
        else:
            right = self.getright().getkey()
        return str(left) + " <-{ " + str(self.getkey()) + " }-> " + str(right)

    def __repr__(self):
        return str(self)

    def getkey(self):
        return self.key

    def setkey(self, key):
        self.key = key

    def getvalue(self):
        return self.value

    def setvalue(self, value):
        self.value = value

    def getleft(self):
        return self.left

    def setleft(self, node):
        if node is not None:
            node.parent = self
        self.left = node

    def getright(self):
        return self.right

    def setright(self, node):
        if node is not None:
            node.parent = self
        self.right = node

    def getparent(self):
        return self.parent

