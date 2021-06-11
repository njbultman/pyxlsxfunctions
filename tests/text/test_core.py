from pyxlsxfunctions.text.core import UPPER, LOWER

# Unit tests for UPPER
def test_UPPER_1():
    assert UPPER('high') == 'HIGH'

def test_UPPER_2():
    assert UPPER(['high', 'low', 'medium']) == ['HIGH', 'LOW', 'MEDIUM']

def test_UPPER_3():
    assert UPPER(0) == None

def test_UPPER_4():
    assert UPPER([0, 1, 'hey']) == None

# Unit tests for LOWER
def test_LOWER_1():
    assert LOWER('HIGH') == 'high'

def test_LOWER_2():
    assert LOWER(['HIGH', 'LOW', 'MEDIUM']) == ['high', 'low', 'medium']

def test_LOWER_3():
    assert UPPER(0) == None

def test_LOWER_4():
    assert UPPER([0, 1, 'HEY']) == None
