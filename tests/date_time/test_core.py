from pyxlsxfunctions.date_time.core import NOW, TODAY

def test_NOW():
    assert type(NOW()) == type('known string')

def test_TODAY():
    assert type(TODAY()) == type('known string')