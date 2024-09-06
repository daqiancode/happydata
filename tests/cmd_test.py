from happydata.cmd import *



def test_run():
    assert run('echo hello') == (0, 'hello\n', '')
    assert run('echo $A' , env={'A':'TEST'}) == (0, 'TEST\n', '')
