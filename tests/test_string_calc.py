import pytest
from string_calc import StringCalc

class TestStringCalc:
    def test_add_method_existance(self):
        calc_obj = StringCalc()
        assert hasattr(calc_obj, "add")

    def test_add_non_string_input(self):
        calc_obj = StringCalc()
        with pytest.raises(Exception) as exc_info:
            calc_obj.add(1)

        assert str(exc_info.value) == "Invalid input for param(s) = [numbers]"

    def test_add_empty_string_input(self):
        calc_obj = StringCalc()
        assert calc_obj.add("") == 0

    def test_add_1_2_input(self):
        calc_obj = StringCalc()
        assert calc_obj.add("1,2") == 3

    def test_add_3_4_input(self):
        calc_obj = StringCalc()
        assert calc_obj.add("3,4") == 7

    def test_add_1_2_3_input(self):
        calc_obj = StringCalc()
        assert calc_obj.add("1\n2,3") == 6

    def test_add_1_2_input_with_custom_delimiters(self):
        calc_obj = StringCalc()
        assert calc_obj.add("//;\n1;2") == 3

    def test_add_1_2_3_input_with_custom_and_newline_delimiters(self):
        calc_obj = StringCalc()
        assert calc_obj.add("//;\n1;2\n3") == 6

    def test_add_1_2_3_input_with_invalid_delimiters(self):
        calc_obj = StringCalc()
        with pytest.raises(Exception) as exc_info:
            calc_obj.add(("//;\n1.2\n3"))

        assert str(exc_info.value) == "Invalid delimiter present in param(s) = [numbers]"
