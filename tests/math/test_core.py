from pyxlsxfunctions.math.core import SUMIF, COUNTIF, AND

#Unit tests for SUMIF
def test_SUMIF_1():
    assert SUMIF([1, 2, 3, 4, 5], ['yes', 'yes', 'no', 'no', 'yes'], 'yes') == 8

def test_SUMIF_2():
    assert SUMIF([1, 2, 3, 4, 5], ['yes', 'yes', 'no', 'no', 'yes'], 1) == None

def test_SUMIF_3():
    assert SUMIF([1, 2, 3, 4, 5], ['yes', 'yes', 'no'], 'yes') == None

#Unit tests for COUNTIF
def test_COUNTIF_1():
    assert COUNTIF([1, 2, 3, 4, 5], ['yes', 'yes', 'no', 'no', 'yes'], 'yes') == 3

def test_COUNTIF_2():
    assert COUNTIF([1, 2, 3, 4, 5], ['yes', 'yes', 'no', 'no', 'yes'], 1) == None

def test_COUNTIF_3():
    assert COUNTIF([1, 2, 3, 4, 5], ['yes', 'yes', 'no'], 'yes') == None

#Unit tests for AND
def test_AND_1():
    assert AND(2 < 10, 5 < 10) == True

def test_AND_2():
    assert AND(2 > 10, 5 < 10) == False

def test_AND_3():
    assert AND(2 > 10, 5 > 10) == False

def test_AND_4():
    assert AND(0, 5 > 10) == None

def test_AND_5():
    assert AND(2 > 10, 1) == None