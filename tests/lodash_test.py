from happydata import *
import pytest


def test_groupby():
    assert groupby([{'a': 1}, {'a': 2}, {'a': 1}], 'a') == {1: [{'a': 1}, {'a': 1}], 2: [{'a': 2}]}


def test_groupby():
    assert groupby([{'a': 1}, {'a': 2}, {'a': 1}], lambda x: x['a']) == {1: [{'a': 1}, {'a': 1}], 2: [{'a': 2}]}

@pytest.mark.parametrize('x,y', [
    ([10, 2,3, 10,3], [10, 2, 3]),
    ([], []),
    (None, None),
])
def test_unique(x,y):
    assert unique(x) == y

@pytest.mark.parametrize('x,p,y', [
    ([1, 2, 3, 4, 5, 6, 7, 8,9,10], 3, [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10]]),
    ([1, 2, 3, 4, 5, 6, 7, 8,9,10], 1, [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]]),
    ([1, 2, 3, 4, 5, 6, 7, 8,9,10], 10, [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]]),
    ([1, 2, 3, 4, 5, 6, 7, 8,9,10], 11, [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]]),
    ([1, 2, 3, 4, 5, 6, 7, 8,9,10], 0, [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]]),
    ([1, 2, 3, 4, 5, 6, 7, 8,9,10], -1, [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]]),
    ([1, 2, 3, 4, 5, 6, 7, 8,9,10], None, [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]]),
])
def test_partition(x,p,y):
    assert list(partition(x,p)) == y

def test_divide():
    assert divide([1, 2, 3, 4, 5, 6, 7, 8,9,10], 3) == [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10]]

@pytest.mark.parametrize('x,y', [
    ([1, [2, 3], [4], [[2]]], [1, 2, 3, 4, [2]]),
    ([1, [2, 3], [4], [[2], [3]]], [1, 2, 3, 4, [2], [3]]),
])
def  test_flattern(x, y):
    assert flattern(x) == y

@pytest.mark.parametrize('x,y', [
    ([1, [2, 3], [4], [[2]]], [1, 2, 3, 4, 2]),
    ([1, [2, 3], [4], [[2], [3]]], [1, 2, 3, 4, 2, 3]),
    ([],[]),
    (None,None)
])
def test_flattern_deep(x,y):
    assert flattern_deep(x) == y

def test_now():
    assert now() > 1725628633

