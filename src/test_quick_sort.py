# _*_ encoding: utf-8 _*_
"""Test Implementation of quicksort Algorithm."""

import random
import pytest
import string

FEW_UNIQUE = list('a' * 25 + 'b' * 25 + 'c' * 25 + 'd' * 25)
random.shuffle(FEW_UNIQUE)

EDGE_CASES = [
    [],  # Empty
    '',  # Empty
    (),  # Empty
    [0],  # One item
    'a',  # One item
    (0, ),  # One item
    list(range(100)),  # Already sorted
    list(range(99, -1, -1)),  # Reversed
    # Almost sorted
    list(range(33)) + [66] + list(range(32, 66)) + [33] + list(range(67, 99)),
    # Few unique
    FEW_UNIQUE,
]


RANDOM_INT_LISTS = [random.sample(range(1000),
                    random.randrange(2, 100)) for n in range(50)]

RANDOM_INT_TUPLES = [tuple(random.sample(range(1000),
                     random.randrange(2, 100))) for n in range(50)]

RANDOM_STRINGS = [random.sample(string.printable,
                  random.randrange(2, 100)) for n in range(50)]

TEST_CASES = EDGE_CASES + RANDOM_INT_LISTS + RANDOM_INT_TUPLES + RANDOM_STRINGS


@pytest.mark.parametrize("seq", TEST_CASES)
def test_quick_sort(seq):
    """Test insertion sort results equal built-in python sort results."""
    from quick_sort import quick_sort
    assert quick_sort(seq) == sorted(seq)


def test_sort_simple():
    """Test on simple manually created explicit case."""
    from quick_sort import quick_sort
    a_list = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    assert quick_sort(a_list) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
