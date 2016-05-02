# _*_ encoding: utf-8 _*_
"""Implement radix sort algorithm in Python.

Works only for lists of positive ints up to specified number of decimal places.
"""


def radix_sort(a_list, places=10):
    """Sort given list in place, for ints up to given decimal places."""
    buckets = [[] for x in range(10)]
    for digit in range(places):
        for number in a_list:
            buckets[number // 10 ** digit % 10].append(number)
        del a_list[:]
        for bucket in buckets:
            a_list.extend(bucket)
            del bucket[:]


if __name__ == "__main__":
    from time_sorting import time_sorting
    time_sorting(radix_sort)
