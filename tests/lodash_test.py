from happydata import *
import pytest

@pytest.mark.parametrize('x,y', [
    ([{'a': 1}, {'a': 2}, {'a': 1}], {1: [{'a': 1}, {'a': 1}], 2: [{'a': 2}]}),
    ([] , {}),
])
def test_groupby(x, y ):
    assert groupby(x, 'a') == y

@pytest.mark.parametrize('x,y', [
    ([],{}),
    ([{'a': 1}, {'a': 2}, {'a': 1}], {1: {'a': 1}, 2: {'a': 2}}),
])
def test_indexby(x,y):
    assert indexby(x,'a') == y

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


@pytest.mark.parametrize('x,k,y', [
    ([{'a': 1}, {'a': 2}, {'a': 1}], 'a', {1: {'a': 1}, 2: {'a': 2}}),
    ([{'a': 1}, {'a': 2}, {'a': 1}], lambda x: x['a'], {1: {'a': 1}, 2: {'a': 2}}),
])
def test_indexby(x, k ,y):
    assert indexby(x, k) == y

@pytest.mark.parametrize('x,keys,y', [
    ({'a': 1, 'b': 2, 'c': 3}, ['a', 'b'], {'a': 1, 'b': 2}),
    ({'a': 1, 'b': 2, 'c': 3}, ['a', 'b', 'd'], {'a': 1, 'b': 2}),
    ({'a': 1, 'b': 2, 'c': 3}, ['a', 'b', 'c'], {'a': 1, 'b': 2, 'c': 3}),
    ({'a': 1, 'b': 2, 'c': 3}, ['a', 'b', 'c', 'd'], {'a': 1, 'b': 2, 'c': 3}),
    ({'a': 1, 'b': 2, 'c': 3}, ['a', 'b', 'c', 'd', 'e'], {'a': 1, 'b': 2, 'c': 3}),
])
def test_pick(x , keys , y ):
    assert pick(x, keys) == y

@pytest.mark.parametrize('x,keys,y', [
    (None, ['a', 'b'], None),
    ({}, ['a', 'b'], {}),
    ({'a': 1, 'b': 2, 'c': 3}, ['a', 'b'], {'c': 3}),
    ({'a': 1, 'b': 2, 'c': 3}, ['a', 'b', 'd'], {'c': 3}),
    ({'a': 1, 'b': 2, 'c': 3}, ['a', 'b', 'c'], {}),
    ({'a': 1, 'b': 2, 'c': 3}, ['a', 'b', 'c', 'd'], {}),
    ({'a': 1, 'b': 2, 'c': 3}, ['a', 'b', 'c', 'd', 'e'], {}),
])
def test_omit(x , keys ,y):
    assert omit(x, keys) == y

def test_shuffle():
    x = list(range(100))
    y = shuffle(x)
    assert x != y
    assert sorted(x) == sorted(y)

def test_sample():
    x = list(range(100))
    y = sample(x, 10)
    assert len(y) == 10
    assert all([i in x for i in y])


def test_randstr():
    assert len(randstr(10)) == 10
    assert len(randstr(10, False)) == 10
    assert len(randstr(10, False,False)) == 10

@pytest.mark.parametrize('x,y', [
    ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [1, 2, 3, 4, 5, 6, 7, 8, 9]),
])
def test_union(x , y):
    assert union(*x) == y

@pytest.mark.parametrize('a,b,y', [
    ([1, 2, 3], [2, 3, 4], [2, 3]),
    ([1, 2, 3], [4, 5, 6], []),
    ([1, 2, 3], [1, 2, 3], [1, 2, 3]),
    ([1, 2, 3], [], []),
    ([], [1, 2, 3], []),
    ([], [], []),
])
def test_intersection(a,b,y):
    assert intersection(a,b) == y

@pytest.mark.parametrize('a,b,y', [
    ([1, 2, 3], [2, 3, 4], [1]),
    ([1, 2, 3], [4, 5, 6], [1, 2, 3]),
    ([1, 2, 3], [1, 2, 3], []),
    ([1, 2, 3], [], [1, 2, 3]),
    ([], [1, 2, 3], []),
    ([], [], []),
])
def test_difference(a,b,y):
    assert difference(a,b) == y


@pytest.mark.parametrize('x,y', [
    ([1, 2, 3], [0, 1,2]),
    ([3, 2, 1], [2, 1, 0]),
    ([], []),
    ([5,2,6,3,33,45] , [1, 3, 0, 2, 4, 5]),
])
def test_argsort(x, y):
    assert argsort(x) == y

@pytest.mark.parametrize('x,lower,upper,y', [
    (1, 2, 3, 2),
    (2, 2, 3, 2),
    (3, 2, 3, 3),
    (4, 2, 3, 3),
    (1, 2, 1, 1),
    (2, 2, 1, 2),
    (3, 2, 1, 2),
])
def test_clamp(x, lower, upper, y):
    assert clamp(x, lower, upper) == y

@pytest.mark.parametrize('x,a,y', [
    (' abc  ', ' ', 'abc'),
    ("aaaaabc", 'a', 'bc'),
    ("aaaaabc", 'ab', 'aaaaabc'),
    ("aaaaabc", 'aa', 'abc'),
    ('abcabc', 'abc', ''),
    ('abxyzyz', 'yz', 'abx'),
    ('abxyzyz', 'xyz', 'abxyzyz'),
    ('abxyzyz', 'z', 'abxyzy'),
])
def test_trim(x,a,y):
    assert trim(x,a) == y

@pytest.mark.parametrize('s,re,y', [
    ('abc', 'a', 'a'),
    ('123abc', r'\d+', '123'),
    ('/a/b/c?xx', r'(/\w+)', '/a'),
])
def test_re_find(s,re,y):
    assert re_find(s,re) == y

@pytest.mark.parametrize('s,re,y', [
    ('123abc', r'(\d+)', ('123',)),
    ('123abc', r'\d+([a-z]+)', ('abc',)),
    ('123abc', r'(\d+)([a-z]+)', ('123','abc')),
    ('/a/b/c', r'(/\w+)(/\w+)', ('/a', '/b')),
])
def test_re_groups(s,re,y):
    assert re_groups(s,re) == y

def test_new_dict():
    assert kv() == {}
    assert kv(a=1, b=None, c=3) == {'a': 1, 'c': 3}