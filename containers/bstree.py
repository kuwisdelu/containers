
from .node import TNode

### A simple binary search tree (BST) class

class BSTree:

    def __init__(self, root = None):
        self.root = root

    def getroot(self):
        return self.root

    def setroot(self, node):
        self.root = node

    def search(self, key):
        """Iteratively searches tree for node x with x.key == key"""
        node = self.getroot()
        while node is not None and key != node.getkey():
            if key < node.getkey():
                node = node.getleft()
            else:
                node = node.getright()
        return node

    def getmin(self):
        """Returns the node with the minimum key"""
        node = self.getroot()
        while node.getleft() is not None:
            node = node.getleft()
        return node

    def getmax(self):
        """Returns the node with the maximum key"""
        node = self.getroot()
        while node.getright() is not None:
            node = node.getright()
        return node

    def successor(self):
        """The successor of a node x is the node with smallest key greater than x.key"""
        current = self.getroot()
        if current.getright() is not None:
            return BSTree(current.getright()).getmin()
        parent = current.getparent()
        while parent is not None and current is parent.getright():
            current = parent
            parent = parent.getparent()
        return parent

    def predecessor(self):
        """The predecessor of a node x is the node with largest key less than x.key"""
        current = self.getroot()
        if current.getleft() is not None:
            return BSTree(current.getleft()).getmax()
        parent = current.getparent()
        while parent is not None and current is parent.getleft():
            current = parent
            parent = parent.getparent()
        return parent

    def insert(self, key, value = None):
        node = TNode(key, value)
        parent = None
        current = self.getroot()
        while current is not None:
            parent = current
            if node.getkey() < current.getkey():
                current = current.getleft()
            else:
                current = current.getright()
        if parent is None:
            self.setroot(node)
        elif node.getkey() < parent.getkey():
            parent.setleft(node)
        else:
            parent.setright(node)

    def delete(self, key):
        node = self.search(key)
        # key not found
        if node is None:
            return
        # no left child
        if node.getleft() is None:
            self.transplant(node, node.getright())
        # no right child
        elif node.getright() is None:
            self.transplant(node, node.getleft())
        else:
            # find successor (node with next largest key)
            successor = BSTree(node.getright()).getmin()
            # handle successor's parent if it lies within a subtree
            if successor.getparent() is not node:
                self.transplant(successor, successor.getright())
                successor.setright(node.getright())
            # transplant successor and update left child
            self.transplant(node, successor)
            successor.setleft(node.getleft())

    def transplant(self, x, y):
        """Replaces subtree rooted at node x with subtree rooted at node y"""
        if x.getparent() is None:
            self.setroot(y)
        elif x is x.getparent().getleft():
            x.getparent().setleft(y)
        else:
            x.getparent().setright(y)

    def __getitem__(self, key):
        node = self.search(key)
        if node is not None:
            return node.getvalue()
        else:
            raise KeyError

    def __setitem__(self, key, value):
        self.insert(key, value)

    def __delitem__(self, key):
        self.delete(key)

    def __contains__(self, key):
        return self.search(key) is not None

    def inorder(self):
        """In-order depth-first traversal (DFS) using a stack"""
        stack = []
        keys = []
        current = self.getroot()
        while len(stack) > 0 or current is not None:
            if current is not None:
                stack.append(current)
                current = current.getleft()
            else:
                current = stack.pop(-1)
                keys.append(current.getkey())
                current = current.getright()
        return keys

    def preorder(self):
        """Pre-order depth-first traversal (DFS) using a stack"""
        stack = []
        keys = []
        stack.append(self.getroot())
        while len(stack) > 0:
            current = stack.pop(-1)
            if current is not None:
                keys.append(current.getkey())
                if current.getright() is not None:
                    stack.append(current.getright())
                if current.getleft() is not None:
                    stack.append(current.getleft())
        return keys

    def levelorder(self):
        """Level-order breadth-first-traversal (DFS) using a queue"""
        queue = []
        keys = []
        queue.append(self.getroot())
        while len(queue) > 0:
            current = queue.pop(0)
            keys.append(current.getkey())
            if current.getleft() is not None:
                queue.append(current.getleft())
            if current.getright() is not None:
                queue.append(current.getright())
        return keys

    def height(self):
        """Calculate height of the tree using a queue"""
        height = 0
        queue = []
        queue.append(self.getroot())
        while len(queue) > 0:
            size = len(queue)
            # pop all nodes at current level and enqueue their children
            for n in range(size):
                current = queue.pop(0)
                if current.getleft() is not None:
                    queue.append(current.getleft())
                if current.getright() is not None:
                    queue.append(current.getright())
            height += 1
        return height

### Test BSTree methods

if __name__ == "__main__":
    x = BSTree()
    x.insert(12)
    x.insert(5)
    x.insert(18)
    x.insert(2)
    x.insert(9)
    x.insert(15)
    x.insert(19)
    x.insert(17)
    x.insert(13)
    print(x.getroot())
    print(x.getmin())
    print(x.getmax())
    print(walk_tree_inorder(x.getroot()))
    print(x.inorder())
    print(walk_tree_preorder(x.getroot()))
    print(x.preorder())
    print(x.height())
    print(walk_tree_level(x.getroot(), 1))
    print(walk_tree_level(x.getroot(), 2))
    print(walk_tree_level(x.getroot(), 3))
    print(walk_tree_level(x.getroot(), 4))
    print(x.levelorder())
    print(x.search(17))
    print(search_tree(x.getroot(), 17))
    print(x.getroot())
    x.delete(12)
    print(x.getroot())
    print(x.inorder())
    x.delete(100)
    print(x.inorder())
    x.delete(18)
    print(x.getroot())
    print(x.inorder())
    y = BSTree()
    y.update([1, 2, 3, 4, 5, 6, 7])
    print(y.inorder())
    print(y.getroot())
    print(y.getroot().getleft())
    print(y.getroot().getright())
    print(y.preorder())




