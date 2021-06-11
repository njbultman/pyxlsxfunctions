from pyxlsxfunctions.date_time.core import NOW, TODAY

# Tests for NOW function
def test_NOW():
    assert type(NOW()) == type('known string')

# Tests for TODAY function
def test_TODAY():
    assert type(TODAY()) == type('known string')