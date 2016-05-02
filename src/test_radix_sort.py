# _*_ encoding: utf-8 _*_
"""Test Implementation of Radix Sort Algorithm."""

import random
import pytest

FEW_UNIQUE = [0] * 25 + [1] * 25 + [2] * 25 + [3] * 25
random.shuffle(FEW_UNIQUE)

EDGE_CASES = [
    [],  # Empty
    [0],  # One item
    list(range(100)),  # Already sorted
    list(range(99, -1, -1)),  # Reversed
    # Almost sorted
    list(range(33)) + [66] + list(range(32, 66)) + [33] + list(range(67, 99)),
    # Few unique
    FEW_UNIQUE,
]

RANDOM_INT_LISTS = [random.sample(range(1000),
                    random.randrange(2, 100)) for n in range(50)]

TEST_CASES = EDGE_CASES + RANDOM_INT_LISTS


@pytest.mark.parametrize("seq", TEST_CASES)
def test_radix_sort(seq):
    """Test radix sort results equal built-in python sort results."""
    from radix_sort import radix_sort
    sorted_copy = sorted(seq)
    radix_sort(seq)
    assert seq == sorted_copy
