from pyxlsxfunctions.date_time.core import NOW, TODAY, DAYS, EOMONTH

# Unit tests for NOW function
def test_NOW():
    assert type(NOW()) == type('known string')

# Unit tests for TODAY function
def test_TODAY():
    assert type(TODAY()) == type('known string')

# Unit tests for DAYS function
def test_DAYS_1():
    assert DAYS('2016-01-01', '2016-01-02') == 1

def test_DAYS_2():
    assert DAYS('2016-01-01', '2016-01-05') == 4

def test_DAYS_3():
    assert DAYS('20160101', '2016-01-02') == None
    
def test_DAYS_3():
    assert DAYS(0, '2016-01-02') == None

# Unit tests for EOMONTH function
def test_EOMONTH_1():
    assert EOMONTH('2016-01-01', 0) == '2016-01-31'

def test_EOMONTH_2():
    assert EOMONTH('2017-01-03', -1) == '2016-12-31'

def test_EOMONTH_3():
    assert EOMONTH('2017-01-03', 3) == '2017-04-30'
    
def test_EOMONTH_4():
    assert EOMONTH('hi', 1) == None

def test_EOMONTH_5():
    assert EOMONTH(['2017-03-01', '2020-09-29'], 0) == ['2017-03-31', '2020-09-30']

def test_EOMONTH_6():
    assert EOMONTH(1, 1) == None

def test_EOMONTH_7():
    assert EOMONTH(['2017-03-01', 'hi'], 0) == None