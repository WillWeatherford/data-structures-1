# _*_ encoding: utf-8 _*_
"""Test trie module."""
import pytest

from trie import ALLOWED_INPUT

INVALID_WORDS = ['lsf', 'mvniersdn', 'adsklieu', 'zqx', 'cdu', 'quc',
                 'aeka-mei', 'cwefmoi\'sadlfmwe']

GROWTH_WORDS = ['set', 'sets', 'setter', 'settle', 'settled', 'settler',
                'settling', 'stow', 'stop', 'stock', 'sty', 'style',
                'stall', 'stomp', 'stag',
                'stalled']


def get_words():
    """Get a big set of values for thorough tests."""
    with open("/usr/share/dict/words", "r") as get_file:
        for line in get_file:
            word = line.strip('\n')
            if set(word).issubset(ALLOWED_INPUT):
                yield word


@pytest.fixture(params=INVALID_WORDS)
def invalid_word(request):
    """Fixture for unacceptable word inputs."""
    return request.param


@pytest.fixture(scope='session')
def all_words():
    """Fixture inserts all words from dictionary into trie."""
    from trie import Trie
    big_trie = Trie()
    for word in get_words():
        big_trie.insert(word)
    return big_trie


@pytest.fixture(params=get_words())
def word_in_dictionary(request):
    """Fixture gets all the words from the dictionary."""
    return request.param


@pytest.fixture
def simple_trie():
    """Fixture makes empty tree."""
    from trie import Trie
    return Trie()


@pytest.fixture
def growth_trie():
    """Return trie populated by similar words."""
    from trie import Trie
    instance = Trie()
    for word in GROWTH_WORDS:
        instance.insert(word)
    return instance


def test_insert_1(simple_trie):
    """Test that we can insert single item into trie."""
    simple_trie.insert('a')
    assert 'a' in simple_trie._dict


def test_insert_2(simple_trie):
    """Test we can insert two words beginning with the same letter."""
    simple_trie.insert('at')
    simple_trie.insert('as')
    assert simple_trie._dict == {'a': {'t': {'$': '$'}, 's': {'$': '$'}}}


def test_trie_structure(simple_trie):
    """Test that trie is well formed."""
    simple_trie.insert('at')
    assert simple_trie._dict == {'a': {'t': {'$': '$'}}}


def test_trie_insert_empty(simple_trie):
    """Test that insert fails without valid content."""
    with pytest.raises(ValueError):
        simple_trie.insert('')


def test_contains_1(simple_trie):
    """Test contains method."""
    simple_trie.insert('bob')
    simple_trie.insert('fred')
    assert simple_trie.contains('fred')


def test_contains_2(simple_trie):
    """Test contains method fails when item not present."""
    simple_trie.insert('bob')
    assert not simple_trie.contains('frank')


def test_dictionary(all_words):
    """Test that after insertion trie contains every word in dictionary."""
    for word in get_words():
        assert all_words.contains(word)


def test_insert_bad_input(simple_trie):
    """Test that insert only works for valid words."""
    with pytest.raises(ValueError):
        simple_trie.insert('asdfj3*&%^$')


def test_insert_bad_input_2(simple_trie):
    """Test that insert fails for invalid data types."""
    with pytest.raises(TypeError):
        simple_trie.insert(['bob', 'fred'])


def test_dictionary_false(all_words, invalid_word):
    """Test trie containing dictionary words does not contain phony words."""
    assert not all_words.contains(invalid_word)


def test_traversal_1(growth_trie):
    """Test depth-first traversal returns generator of dissimilar words."""
    for item in GROWTH_WORDS:
        assert item in list(growth_trie.traversal())


def test_traversal_2(simple_trie):
    """Test traversal method on empty trie."""
    assert list(simple_trie.traversal()) == []


def test_traversal_3(growth_trie):
    """Test that traversal does not return item not in trie."""
    assert 'valid' not in list(growth_trie.traversal())


def test_traversal_4(growth_trie):
    """Test traversal gives us the right number of items."""
    assert len(GROWTH_WORDS) == len(list(growth_trie.traversal()))


def test_traversal_5(growth_trie):
    """Test depth-first traversal.

    It should return generator of inserted words with identical starts.
    """
    assert set(growth_trie.traversal()) == set(GROWTH_WORDS)


def test_traversal_6(growth_trie):
    """Test that we can begin traversal from a given valid start value."""
    assert set(growth_trie.traversal('sto')) == set(['stomp', 'stow',
                                                     'stock', 'stop'])


def test_traversal_7(growth_trie):
    """Test that beginning traversal from bad start value raises error."""
    with pytest.raises(ValueError):
        list(growth_trie.traversal('x'))


def test_traversal_depth_first(growth_trie):
    """Test that traversal is depth-first."""
    output = list(growth_trie.traversal())
    assert output[0][:2] == output[0][:2]


# def test_a_word(all_words, word_in_dictionary):
#     """For fun, separate test for each word in dictionary."""
#     assert all_words.contains(word_in_dictionary)
