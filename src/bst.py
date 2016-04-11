# _*_ encoding: utf-8 _*_
"""Binary Search Tree Implementation."""
from queue import Queue
import random
import time


class Bst(object):
    """Implement Binary Search Tree."""

    def __init__(self, value=None, parent=None, left_child=None,
                 right_child=None):
        """Init Tree."""
        self.value = value
        self.parent = parent
        self.left_child = left_child
        self.right_child = right_child

    @property
    def left_child(self):
        """Left child."""
        return self._left_child

    @left_child.setter
    def left_child(self, other_node):
        self._left_child = other_node
        if other_node is not None:
            other_node.parent = self

    @property
    def right_child(self):
        """Right child."""
        return self._right_child

    @right_child.setter
    def right_child(self, other_node):
        self._right_child = other_node
        if other_node is not None:
            other_node.parent = self

    def _children(self):
        """Yield any children which are not None."""
        for child in (self.left_child, self.right_child):
            if child is not None:
                yield child

    def insert(self, value):
        """Insert value into tree if not present."""
        if self.contains(value):
            return
        if self.value is None:
            self.value = value
        try:
            if value > self.value:
                if not self.right_child:
                    self.right_child = Bst(parent=self, value=value)
                else:
                    self.right_child.insert(value)
            elif value < self.value:
                if not self.left_child:
                    self.left_child = Bst(parent=self, value=value)
                else:
                    self.left_child.insert(value)
        except TypeError:
            raise TypeError("Cannot mix types in a binary search tree.")

    def _search(self, value):
        """Search for value in tree."""
        if self.value == value:
            return self
        left_contains = None
        right_contains = None
        if self.left_child is not None:
            left_contains = self.left_child._search(value)
        if self.right_child is not None:
            right_contains = self.right_child._search(value)
        return left_contains or right_contains

    def contains(self, value):
        """Return True if value in tree."""
        return bool(self._search(value))

    def size(self):
        """Return size of tree."""
        if self.value is None:
            return 0
        if not self.left_child and not self.right_child:
            return 1
        sizes = [child.size()
                 for child in (self.left_child, self.right_child)
                 if child is not None]
        return sum(sizes) + 1

    def depth(self):
        """Return number of levels in the tree."""
        if self.value is None:
            return 0
        if not self.left_child and not self.right_child:
            return 1
        depths = [child.depth()
                  for child in (self.left_child, self.right_child)
                  if child is not None]
        return max(depths) + 1

    def balance(self):
        """Return number expressing balance or lack thereof of tree."""
        left_depth = 0
        right_depth = 0
        if self.left_child is not None:
            left_depth = self.left_child.depth()
        if self.right_child is not None:
            right_depth = self.right_child.depth()
        return left_depth - right_depth

    def in_order(self):
        """Traverse tree with in-order traversal."""
        if self.left_child is not None:
            for item in self.left_child.in_order():
                yield item
        if self.value is not None:
            yield self.value
        if self.right_child is not None:
            for item in self.right_child.in_order():
                yield item

    def pre_order(self):
        """Traverse tree with pre-order traversal."""
        if self.value is not None:
            yield self.value
        if self.left_child is not None:
            for item in self.left_child.pre_order():
                yield item
        if self.right_child is not None:
            for item in self.right_child.pre_order():
                yield item

    def post_order(self):
        """Traverse tree with post-order traversal."""
        if self.left_child is not None:
            for item in self.left_child.post_order():
                yield item
        if self.right_child is not None:
            for item in self.right_child.post_order():
                yield item
        if self.value is not None:
            yield self.value

    def breadth_first(self):
        """Traverse tree with breadth-first traversal."""
        q = Queue()
        q.enqueue(self)
        while q.size() > 0:
            print(q.size())
            tree = q.dequeue()
            if tree.value is not None:
                yield tree.value
            if tree.left_child is not None:
                q.enqueue(tree.left_child)
            if tree.right_child is not None:
                q.enqueue(tree.right_child)

    def delete(self, value):
        """Delete value from tree."""
        deletable = self._search(value)
        if not deletable:
            return
        if deletable.parent is not None:
            if deletable.parent.left_child == deletable:
                deletable.parent.left_child = None
            elif deletable.parent.right_child == deletable:
                deletable.parent.right_child = None
            deletable.parent = None
            for value in deletable.breadth_first():
                if value != deletable.value:
                    self.insert(value)
        else:
            if self.right_child.size() > self.left_child.size():
                largest_child = self.right_child
                insertable = self.left_child
            else:
                largest_child = self.left_child
                insertable = self.right_child
            self.right_child = largest_child.right_child
            self.left_child = largest_child.left_child
            self.value = largest_child.value
            self.parent = None
            del largest_child
            for value in insertable.breadth_first():
                self.insert(value)
            del insertable


if __name__ == "__main__":
    values = random.sample(range(1000), 100)
    big_tree = Bst()
    for val in values:
        big_tree.insert(val)
    search_val = random.choice(values)

    timescores = []
    for n in range(1000):
        start = time.time()
        big_tree.contains(search_val)
        delta = time.time() - start
        timescores.append((delta, search_val))

    timescores.sort()
    print("The fastest search took {} seconds for {}".format(*timescores[0]))
    print("The slowest search took {} seconds for {}".format(*timescores[-1]))
