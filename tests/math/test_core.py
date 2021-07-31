from pyxlsxfunctions.math.core import SUMIF, COUNTIF, AND, OR, IF, FV, PV, AVERAGE, LEN, VLOOKUP, CORREL, AVERAGEIF, COUNTBLANK
import numpy as np
import pandas as pd

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

# Unit tests for LEN
def test_LEN_1():
    assert LEN(['hi', 'hey', 'hoho']) == [2, 3, 4]

def test_LEN_2():
    assert LEN('hi') == 2

def test_LEN_3():
    assert LEN(1) == None

def test_LEN_4():
    assert LEN(1.0) == None

def test_LEN_5():
    assert LEN(['hi', 1.0]) == None

# Unit tests for VLOOKUP
def test_VLOOKUP_1():
    assert type(VLOOKUP(["Nick", "Jake", "Tyler", "Nate"], pd.DataFrame({'name': ["Nick", "Jake", "Tyler", "Nate"], 'number':[1, 2, 3, 4]}), "name", 1)) == pd.core.frame.DataFrame

def test_VLOOKUP_2():
    assert VLOOKUP(["Nick", "Jake", "Tyler", "Nate"], pd.DataFrame({'name': ["Nick", "Jake", "Tyler", "Nate"], 'number':[1, 2, 3, 4]}), "name", 2) == None

def test_VLOOKUP_3():
    assert VLOOKUP(["Nick", "Jake", "Tyler", "Nate"], [1, 2, 3 ,4], "name", 2) == None

# Unit tests for CORREL
def test_CORREL_1():
    assert round(CORREL([1, 2, 3, 4], [2, 7, 1, 12]), 2) == 0.61

def test_CORREL_2():
    assert CORREL(['hi', 2, 3, 4], [2, 7, 1, 12]) == None

def test_CORREL_3():
    assert CORREL([1, 2, 3, 4], [2, 'hi', 1, 12]) == None

# Unit tests for AVERAGEIF
def test_AVERAGEIF_1():
    assert AVERAGEIF([1, 2, 3, 4, 5], ['yes', 'yes', 'no', 'yes', 'yes'], 'yes') == 3.0

def test_AVERAGEIF_2():
    assert AVERAGEIF([1, 2, 3, 4, 5], ['yes', 'yes', 'no', 'no', 'yes'], 1) == None

def test_AVERAGEIF_3():
    assert AVERAGEIF([1, 2, 3, 4, 5], ['yes', 'yes', 'no'], 'yes') == None

# Unit tests for COUNTBLANK
def test_COUNTBLANK_1():
    assert COUNTBLANK(['', '', 2]) == 2

def test_COUNTBLANK_2():
    assert COUNTBLANK(2) == None

def test_COUNTBLANK_3():
    assert COUNTBLANK(['', 1, 'hi']) == 1

def test_COUNTBLANK_4():
    assert COUNTBLANK(['', '', '']) == 3

def test_COUNTBLANK_5():
    assert COUNTBLANK([20, 1, 2]) == 0

def test_COUNTBLANK_6():
    assert COUNTBLANK('hey') == None




