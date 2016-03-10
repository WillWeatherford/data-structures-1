# _*_ encoding: utf-8 _*_
import pytest
"""Test queue.py."""

SIZE = [(['one', 'two', 'three', 'four'], 4)]
PEEK = [(['one', 'two', 'three', 'four'], 'one')]
DEQUEUE = [(['one', 'two', 'three', 'four'])]
ENQUEUE = [(['one', 'two', 'three'], 'three')]


def test_inheritance():
    """Test init from queue."""
    from doubly_linked import DoublyLinked
    from queue import Queue
    new_list = Queue()
    assert isinstance(new_list._container, DoublyLinked)
