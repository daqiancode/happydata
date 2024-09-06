
from happydata.transform import *


def test_groupby():
    assert groupby([{'a': 1}, {'a': 2}, {'a': 1}], 'a') == {1: [{'a': 1}, {'a': 1}], 2: [{'a': 2}]}


def test_groupby_fn():
    assert groupby_fn([{'a': 1}, {'a': 2}, {'a': 1}], lambda x: x['a']) == {1: [{'a': 1}, {'a': 1}], 2: [{'a': 2}]}


def test_unique():
    assert unique([3,1, 2, 1, 2, 3]) ==  [3, 1, 2]