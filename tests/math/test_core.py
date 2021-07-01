from pyxlsxfunctions.math.core import SUMIF, COUNTIF, AND, OR, IF, FV, PV, AVERAGE
import numpy as np

# Unit tests for SUMIF
def test_SUMIF_1():
    assert SUMIF([1, 2, 3, 4, 5], ['yes', 'yes', 'no', 'no', 'yes'], 'yes') == 8

def test_SUMIF_2():
    assert SUMIF([1, 2, 3, 4, 5], ['yes', 'yes', 'no', 'no', 'yes'], 1) == None

def test_SUMIF_3():
    assert SUMIF([1, 2, 3, 4, 5], ['yes', 'yes', 'no'], 'yes') == None

# Unit tests for COUNTIF
def test_COUNTIF_1():
    assert COUNTIF([1, 2, 3, 4, 5], ['yes', 'yes', 'no', 'no', 'yes'], 'yes') == 3

def test_COUNTIF_2():
    assert COUNTIF([1, 2, 3, 4, 5], ['yes', 'yes', 'no', 'no', 'yes'], 1) == None

def test_COUNTIF_3():
    assert COUNTIF([1, 2, 3, 4, 5], ['yes', 'yes', 'no'], 'yes') == None

# Unit tests for AND
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

# Unit tests for OR
def test_OR_1():
    assert OR(2 < 10, 5 < 10) == True

def test_OR_2():
    assert OR(2 > 10, 5 < 10) == True

def test_OR_3():
    assert OR(2 > 10, 5 > 10) == False

def test_OR_4():
    assert OR(0, 5 > 10) == None

def test_OR_5():
    assert OR(2 > 10, 1) == None

# Unit tests for IF
def test_IF_1():
    assert IF(2 < 5, 'yes', 'no') == 'yes'

def test_IF_2():
    assert IF(2 > 5, 'yes', 'no') == 'no'

def test_IF_3():
    assert IF(5, 'yes', 'no') == None

# Unit tests for FV
def test_FV_1():
    assert round(FV(0.1, 3, [50, 100, 150], 100), 2) == round(100 * 1.1**3 + 50 * 1.1**2 + 100*1.1 + 150, 2)

def test_FV_2():
    assert FV(0.01, 2, [50, 100, 150], 100) == None

def test_FV_3():
    assert FV(0.01, -2, [50, 100, 150], 100) == None

def test_FV_4():
    assert round(FV(0.1, 1, 0, 100), 2) == round(100 * 1.1, 2)

# Unit tests for PV
def test_PV_1():
    assert round(PV(0.1, 3, [50, 100, 150], 100), 2) == round(100 / 1.1**3 + 150 / 1.1**3 + 100/1.1**2 + 50/1.1, 2)

def test_PV_2():
    assert PV(0.01, 2, [50, 100, 150], 100) == None

def test_PV_3():
    assert PV(0.01, -2, [50, 100, 150], 100) == None

def test_PV_4():
    assert round(PV(0.1, 1, 0, 100), 2) == 90.91

# Unit tests for AVERAGE
def test_AVERAGE_1():
    assert AVERAGE([1, 2, 3]) == 2.0

def test_AVERAGE_2():
    assert AVERAGE(np.array([1, 2, 3])) == 2.0

def test_AVERAGE_3():
    assert AVERAGE(1) == None





