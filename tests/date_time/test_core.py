from pyxlsxfunctions.date_time.core import NOW, TODAY, DAYS

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