# _*_ encoding: utf-8 _*_
"""Test heap.py."""

import math

heap = [16, 14, 10, 8, 7, 9, 3, 2, 4, 1]


def test_inheritance():
    """Test init from heap."""
    from heap import Heap
    from heap import Heap_Tools
    new_heap = Heap()
    assert isinstance(new_heap._container, Heap_Tools)



# def test_heapify(A, i):
#     assert(False)


def test_root_parent():
    from heap import Heap
    new_heap = Heap(heap)
    assert new_heap._container.parent(new_heap, 0) == None
    print("pass")


# def test_a_parent():
#     assert(False)


# def test_a_left():
#     left(i)


# def test_a_right():
#     assert(False)


# def test_push():
#     n = 11
#     assert(False)


# def test_pop():
#     asset(False)


