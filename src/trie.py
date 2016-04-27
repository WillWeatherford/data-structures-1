# _*_ encoding: utf-8 _*_
"""Implement a trie structure in Python."""
import string

WORD_TERMINUS = '$'

ALLOWED_INPUT = string.ascii_letters + "'-"


class Trie(object):
    """Make a trie structure."""

    def __init__(self):
        """Start the trie."""
        self._dict = {}

    def _input_check(self, token):
        """Check input type and value."""
        if not isinstance(token, str):
            raise TypeError('trie can only contain strings')
        if not token:
            raise ValueError('trie must contain a word')
        if not set(token).issubset(ALLOWED_INPUT):
            raise ValueError('trie only contains real words')

    def insert(self, token):
        """Insert item into trie."""
        self._input_check(token)
        current_dict = self._dict
        for letter in token:
            current_dict = current_dict.setdefault(letter, {})
        current_dict[WORD_TERMINUS] = WORD_TERMINUS

    def contains(self, token):
        """Check if word is contained in trie."""
        self._input_check(token)
        current_dict = self._dict
        try:
            for letter in token:
                current_dict = current_dict[letter]
            return current_dict[WORD_TERMINUS] == WORD_TERMINUS
        except KeyError:
            return False

    def traversal(self, start='', current_dict=None):
        """Return all the words in the trie."""
        # import pdb; pdb.set_trace()
        print('entering new traversal round')
        if current_dict is None:
            current_dict = self._dict.copy()
        for letter in current_dict:
            print(letter)
            print(current_dict[letter])
            if letter == WORD_TERMINUS:
                yield start
            else:
                for item in self.traversal(
                        start + letter, current_dict[letter]):
                    yield item
