import pytest
from string_calc import StringCalc

class TestStringCalc:
    def test_add_method_existance(self):
        calc_obj = StringCalc()
        assert hasattr(calc_obj, "add")

    def test_add_non_string_input(self):
        calc_obj = StringCalc()
        with pytest.raises(Exception):
            calc_obj.add(1)
