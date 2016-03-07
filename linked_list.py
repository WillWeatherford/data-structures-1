# _*_ encoding: utf-8 _*_
"""Demonstrate linked list in python."""


class LinkedList(object):
    """Demonstrate linked list."""

    def __init__(self, head=None):
        """Initialize the list."""
        self.head = head

    def insert(self, val):
        """Insert value at head of list."""
        pass

    def pop():
        """Pop the first value off the head of the list and return it."""
        pass

    def size():
        """Return the length of the list."""
        pass

    def search(self, val):
        """Return the node containing 'val' in list if exists, else None."""
        pass

    def remove(self, node):
        """Remove given node from list."""
        pass

    def display():
        """Print list represented as Python tuple literal."""
        pass


class Node(object):
    """Node constructor for linked list."""

    def __init__(self, data=None, next_node=None):
        """Initialize the node."""
        self.data = data
        self.next_node = next_node

    def get_data(self):
        """Get data for node."""
        return self.data

    def get_next(self):
        """Retrieve next node in list."""
        return self.next_node

    def set_next(self, new_next):
        """Set next node in list."""
        self.next_node = new_next



