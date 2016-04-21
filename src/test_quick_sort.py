# _*_ encoding: utf-8 _*_
"""Test Implementation of quicksort Algorithm."""

import random
import pytest

RANDOM_INSTANCES = [random.sample(range(1000),
                    random.randrange(2, 4)) for n in range(50)]


@pytest.mark.parametrize("seq", RANDOM_INSTANCES)
def test_quick_sort(seq):
    """Test insertion sort results equal built-in python sort results."""
    from quick_sort import quick_sort
    assert quick_sort(seq) == sorted(seq)


def test_sort_simple():
    """Test on simple case."""
    from quick_sort import quick_sort
    a_list = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    assert quick_sort(a_list) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


def test_stable():
    """Test identical items in list retain stable position on sort."""
    from quick_sort import quick_sort
    check_list = [1, 0, 2, 3, 2]
    two_a = check_list[2]
    two_b = check_list[4]
    check_list = quick_sort(check_list)
    assert check_list[2] is two_a
    assert check_list[3] is two_b


@pytest.mark.parametrize("seq", RANDOM_INSTANCES)
def test_stable_random(seq):
    """Test stability property on random lists."""
    from quick_sort import quick_sort
    index_a, index_b = sorted(random.sample(range(len(seq)), 2))
    val_a, val_b = -1, -1
    seq[index_a], seq[index_b] = val_a, val_b
    seq = quick_sort(seq)
    assert seq[0] is val_a
    assert seq[1] is val_b


@pytest.mark.parametrize("seq", RANDOM_INSTANCES)
def test_stable_random_2(seq):
    """Test that stability is maintained when sorting to end of list."""
    from quick_sort import quick_sort
    if len(seq) < 3:
        return
    index_a, index_b = sorted(random.sample(range(len(seq)), 2))
    val_a, val_b = 1000, 1000
    seq[index_a], seq[index_b] = val_a, val_b
    seq = quick_sort(seq)
    assert seq[-1] is val_b
    assert seq[-2] is val_a


@pytest.mark.parametrize("seq", RANDOM_INSTANCES)
def test_stable_random_3(seq):
    """Test stability property on random lists with random duplicate values."""
    from quick_sort import quick_sort
    if len(seq) < 4:
        return
    index_a = random.randrange(len(seq) - 1)
    index_b = random.randrange(index_a + 1, len(seq))
    val_a = seq[index_a]
    val_b = int(val_a)
    seq[index_b] = val_b
    seq = quick_sort(seq)
    index_a = seq.index(val_a)
    assert seq[index_a + 1] is val_b

