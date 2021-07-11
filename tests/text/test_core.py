from pyxlsxfunctions.text.core import UPPER, LOWER, LEFT, RIGHT, TRIM, FIND
import numpy as np

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

# Unit tests for TRIM
def test_TRIM_1():
    assert TRIM('   hi') == 'hi'

def test_TRIM_2():
    assert TRIM('hi    ') == 'hi'

def test_TRIM_3():
    assert TRIM(['hey   ', '  hi  ', '  heyhey ', 'testy   ']) == ['hey', 'hi', 'heyhey', 'testy']

def test_TRIM_4():
    assert TRIM(1) == None

def test_TRIM_5():
    assert TRIM([0, '  hi', 'hey ']) == None

# Unit tests for FIND
def test_FIND_1():
    assert FIND('h', 'hi') == 0

def test_FIND_2():
    assert FIND('h', ['hi', 'iih']) == [0, 2]

def test_FIND_3():
    assert FIND('h', ['hi', 'iih', 'i']) == [0, 2, np.nan]

def test_FIND_4():
    assert FIND('h', ['hi', 'iih', 0]) == None

def test_FIND_5():
    assert FIND('h', 2) == None

def test_FIND_6():
    assert FIND(0, 'hi') == None

def test_FIND_7():
    assert FIND('hi', 'hiiiii') == None
