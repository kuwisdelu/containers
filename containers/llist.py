
from .node import LNode

### A simple linked list implementation

class LList:

    def __init__(self):
        self.head = None

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node.getdata()
            node = node.getnext()

    def __str__(self):
        return " -> ".join([str(x) for x in self])

    def __len__(self):
        size = 0
        for i in self:
            size += 1
        return size

    def append(self, value):
        newnode = LNode(value, None)
        if self.head is None:
            self.head = newnode
        else:
            tail = self.head
            while tail.getnext() is not None:
                tail = tail.getnext()
            tail.setnext(newnode)

    def get(self, index):
        node = self.head
        current = 0
        while node is not None:
            if current == index:
                return node.getdata()
            node = node.getnext()
            current += 1
        raise IndexError

    def set(self, index, value):
        node = self.head
        current = 0
        while node is not None:
            if current == index:
                node.setdata(value)
                return
            node = node.getnext()
            current += 1
        raise IndexError

    def insert(self, index, value):
        node = self.head
        current = 0
        if index == 0:
            if node is not None:
                self.head = LNode(value, node)
            else:
                raise IndexError
        else:
            while node is not None:
                if current == index:
                    break
                prev = node
                node = node.getnext()
                current += 1
            if node is not None:
                prev.setnext(LNode(value, node))
            else:
                if current == index - 1:
                    prev.setnext(LNode(value, None))
                else:
                    raise IndexError

    def delete(self, index):
        node = self.head
        current = 0
        if index == 0:
            if node is not None:
                self.head = node.getnext()
            else:
                raise IndexError
        else:
            while node is not None:
                if current == index:
                    break
                prev = node
                node = node.getnext()
                current += 1
            if node is not None:
                prev.setnext(node.getnext())
            else:
                raise IndexError

    def index(self, value):
        if self.head is None:
            raise ValueError
        else:
            index = 0
            node = self.head
            while node is not None:
                if node.getdata() == value:
                    return index
                node = node.getnext()
            raise ValueError

    def __getitem__(self, index):
        return self.get(index)

    def __setitem__(self, index, value):
        self.set(index, value)

    def __delitem__(self, index):
        self.delete(index)

    def __contains__(self, key):
        try:
            self.index(key)
            return True
        except ValueError:
            return False

