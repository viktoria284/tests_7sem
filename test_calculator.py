import pytest
from calculator import Calculator

class TestCalculator:
    def setup_method(self):
        self.calc = Calculator()

    def test_add_positive_numbers(self):
        assert self.calc.add(2, 3) == 5

    def test_add_negative_numbers(self):
        assert self.calc.add(-1, -1) == -2

    def test_divide_normal(self):
        assert self.calc.divide(6, 2) == 3

    def test_divide_by_zero(self):
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            self.calc.divide(5, 0)

    @pytest.mark.parametrize("number, expected", [
        (2, True),
        (3, True),
        (4, False),
        (1, False),
        (0, False),
        (-5, False),
        (13, True),
        (15, False),
    ])
    def test_is_prime_number(self, number, expected):
        assert self.calc.is_prime_number(number) == expected