
from happydata import *


def test_groupby():
    assert groupby([{'a': 1}, {'a': 2}, {'a': 1}], 'a') == {1: [{'a': 1}, {'a': 1}], 2: [{'a': 2}]}


def test_groupby_fn():
    assert groupby_fn([{'a': 1}, {'a': 2}, {'a': 1}], lambda x: x['a']) == {1: [{'a': 1}, {'a': 1}], 2: [{'a': 2}]}


def test_unique():
    assert unique([3,1, 2, 1, 2, 3]) ==  [3, 1, 2]

def test_partition():
    assert list(partition([1, 2, 3, 4, 5, 6, 7, 8], 3)) == [[1, 2, 3], [4, 5, 6], [7, 8]]
    for p in partition(read_lines('setup.py'), 3):
        print(p)

def test_divide():
    assert divide([1, 2, 3, 4, 5, 6, 7, 8,9,10], 3) == [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10]]