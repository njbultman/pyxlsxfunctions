from pyxlsxfunctions.text.core import UPPER, LOWER, LEFT, RIGHT

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

# Unit tests for LEFT
def test_LEFT_1():
    assert LEFT('hi', -1) == None

def test_LEFT_2():
    assert LEFT('hi', 1) == 'h'

def test_LEFT_3():
    assert LEFT(['hey', 'hi', 'heyhey', 'testy'], 3) == ['hey', 'hi', 'hey', 'tes']

def test_LEFT_4():
    assert LEFT(1234, 2) == None

def test_LEFT_5():
    assert LEFT('1234', 2) == '12'

# Unit tests for RIGHT
def test_RIGHT_1():
    assert RIGHT('hi', -1) == None

def test_RIGHT_2():
    assert RIGHT('hi', 1) == 'i'

def test_RIGHT_3():
    assert RIGHT(['hey', 'hi', 'heyhey', 'testy'], 3) == ['hey', 'hi', 'hey', 'sty']

def test_RIGHT_4():
    assert RIGHT(1234, 2) == None

def test_RIGHT_5():
    assert RIGHT('1234', 2) == '34'
