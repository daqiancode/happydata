from happydata.io import *
import pytest,io
from pathlib import Path

class User:
    def __init__(self, name:str, age:int):
        self.name = name
        self.age = age

def test_user_jsonl():
    tmp_path = Path('tests/test_users.jsonl')
    to_jsonl([User('name', 18), User('张三', 19)], tmp_path)
    assert load_jsonl(tmp_path) == [{'name': 'name', 'age': 18}, {'name': '张三', 'age': 19}]
    tmp_path.unlink(tmp_path)

def test_jsonl():
    tmp_path = Path('tests/test.jsonl')
    to_jsonl([{'a': 1}, {'b': 2}], tmp_path)
    assert load_jsonl(tmp_path) == [{'a': 1}, {'b': 2}]
    tmp_path.unlink(tmp_path)


def test_gz_json():
    tmp_path = Path('tests/test.jsonl.gz')
    to_jsonl_gz([{'a': 1}, {'b': 2}], tmp_path)
    assert load_jsonl_gz(tmp_path) == [{'a': 1}, {'b': 2}]
    tmp_path.unlink(tmp_path)

def test_lines():
    tmp_path = Path('tests/test.txt')
    write_lines(['a', 'b', 'c'],tmp_path)
    assert list(read_lines(tmp_path)) == ['a', 'b', 'c']
    tmp_path.unlink(tmp_path)

def test_tar_gz():
    tmp_path = Path('tests/test.tar.gz')
    write_tar_gz(tmp_path, {
        'a.txt': io.BytesIO(b'hello'),
    })
    for item, f in read_tar_gz(tmp_path):
        assert item.name == 'a.txt'
        assert f.read() == b'hello'
    
    tmp_path.unlink(tmp_path)

def test_zip():
    tmp_path = Path('tests/test.zip')
    write_zip(tmp_path, {
        'a.txt': io.BytesIO(b'hello'),
    })
    for name, f in read_zip(tmp_path):
        assert name == 'a.txt'
        assert f.read() == b'hello'
    tmp_path.unlink(tmp_path)