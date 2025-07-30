from happydata.io import *
import pytest,io
from pathlib import Path

class User:
    def __init__(self, name:str, age:int):
        self.name = name
        self.age = age

def test_user_jsonl():
    tmp_path = Path('tests/test_users.jsonl')
    write_jsonl([User('name', 18), User('张三', 19)], tmp_path)
    assert load_jsonl(tmp_path) == [{'name': 'name', 'age': 18}, {'name': '张三', 'age': 19}]
    tmp_path.unlink(tmp_path)

def test_jsonl():
    tmp_path = Path('tests/test.jsonl')
    write_jsonl([{'a': 1}, {'b': 2}], tmp_path)
    assert load_jsonl(tmp_path) == [{'a': 1}, {'b': 2}]
    tmp_path.unlink(tmp_path)
    tmp_path = Path('tests/test.jsonl.gz')
    write_jsonl([{'a': 1}, {'b': 2}], tmp_path)
    assert load_jsonl(tmp_path) == [{'a': 1}, {'b': 2}]
    tmp_path.unlink(tmp_path)

def test_gz_jsonl():
    tmp_path = Path('tests/test.jsonl.gz')
    write_jsonl_gz([{'a': 1}, {'b': 2}], tmp_path)
    assert load_jsonl_gz(tmp_path) == [{'a': 1}, {'b': 2}]
    tmp_path.unlink(tmp_path)

def test_lines():
    tmp_path = Path('tests/test.txt')
    write_lines(['a', 'b', 'c'],tmp_path)
    assert list(read_lines(tmp_path)) == ['a', 'b', 'c']
    tmp_path.unlink(tmp_path)
    tmp_path = Path('tests/test.txt.gz')
    write_lines(['a', 'b', 'c'],tmp_path)
    assert load_lines(tmp_path) == ['a', 'b', 'c']
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


def test_text():
    tmp_path = Path('tests/test.txt')
    write_text('hello', tmp_path)
    assert load_text(tmp_path) == 'hello'
    tmp_path.unlink(tmp_path)
    tmp_path = Path('tests/test.txt.gz')
    write_text('hello', tmp_path)
    assert load_text(tmp_path) == 'hello'
    tmp_path.unlink(tmp_path)


def test_json():
    tmp_path = Path('tests/test.json')
    write_json({'a': 1}, tmp_path)
    assert load_json(tmp_path) == {'a': 1}
    tmp_path.unlink(tmp_path)
    tmp_path = Path('tests/test.json.gz')
    write_json({'a': 1}, tmp_path)
    assert load_json(tmp_path) == {"a": 1}
    tmp_path.unlink(tmp_path)

def test_dir():
    print(load_dir("/Users/daqian.zhang"))
    assert load_dir(".", suffix=["setup.py"])[0].endswith("setup.py")


def test_tar():
    tmp_path = Path('tests/test.tar')
    write_tar(tmp_path, {
        'a.txt': io.BytesIO(b'hello'),
    })
    for item, f in read_tar(tmp_path):
        assert item.name == 'a.txt'
        assert f.read() == b'hello'
    tmp_path.unlink(tmp_path)

def test_jsonl_append():
    tmp_path = Path('tests/test.jsonl')
    write_jsonl([{'a': 1}], tmp_path)
    write_jsonl([{'b': 2}], tmp_path, append=True)
    assert load_jsonl(tmp_path) == [{'a': 1}, {'b': 2}]
    tmp_path.unlink(tmp_path)

def test_lines_append():
    tmp_path = Path('tests/test.txt')
    write_lines(['a'], tmp_path)
    write_lines(['b'], tmp_path, append=True)
    assert load_lines(tmp_path) == ['a', 'b']
    tmp_path.unlink(tmp_path)

def test_text_append():
    tmp_path = Path('tests/test.txt')
    write_text('a', tmp_path)
    write_text('b', tmp_path, append=True)