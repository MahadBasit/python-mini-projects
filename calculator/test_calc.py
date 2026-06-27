from calc import calc
import pytest

def test_calc_values():
    assert calc(60, 60, "+") == 120
    assert calc(2, 3, "*") == 6
    assert calc(10, 4, "-") == 6
    assert calc(9, 3, "/") == 3

def test_calc_errors():
    with pytest.raises(ZeroDivisionError):
        calc(2, 0,"/")
