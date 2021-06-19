from pyxlsxfunctions.date_time.core import NOW, TODAY

# Unit tests for NOW function
def test_NOW():
    assert type(NOW()) == type('known string')

# Unit tests for TODAY function
def test_TODAY():
    assert type(TODAY()) == type('known string')