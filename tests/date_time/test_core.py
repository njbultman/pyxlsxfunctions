from pyxlsxfunctions.date_time.core import NOW

def test_NOW():
    assert type(NOW()) == type('known string')