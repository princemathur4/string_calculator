from string_calc import StringCalc

class TestStringCalc:
    def test_add(self):
        calc_obj = StringCalc()
        assert hasattr(calc_obj, "add")