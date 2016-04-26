# _*_ encoding: utf-8 _*_
"""Simple implementation of a hash table."""


class HashTable(object):
    """Sample Python Hash Table."""

    def __init__(self, slots):
        """Init method for hash table."""
        self.slots = slots
        self._table = [[] for num in range(slots)]

    def _hash(self, key):
        """Render key string as integer with additive algorithm."""
        hashnum = sum(ord(char) for char in key)
        return hashnum % self.slots

    def set(self, key, value):
        """Store given value in table using given key."""
        if not isinstance(key, str):
            raise TypeError('Hash table only accepts strings as keys.')
        hashed_key = self._hash(key)
        bucket = self._table[hashed_key]
        try:
            bucket.remove((key, value))
        except ValueError:
            pass
        bucket.append((key, value))

    def get(self, key):
        """Retrieve value from table given key."""
        if not isinstance(key, str):
            raise TypeError('Hash table only accepts strings as keys.')
        hashed_key = self._hash(key)
        for tag, value in self._table[hashed_key]:
            if key == tag:
                return value
        return None
