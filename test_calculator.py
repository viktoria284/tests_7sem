import pytest
from calculator import Calculator

class TestCalculator:
    def setup_method(self):
        self.calc = Calculator()

    @pytest.mark.parametrize("a, b, expected", [ 
        (2, 3, 5), 
        (-1, 1, 0), 
        (0, 0, 0), 
        (100, 200, 300), 
        (-5, -3, -8), 
        (2.5, 3.1, 5.6), 
    ]) 
    def test_add(self, a, b, expected): 
        assert self.calc.add(a, b) == expected 
 
    @pytest.mark.parametrize("a, b, expected", [ 
        (10, 2, 5), 
        (9, 3, 3), 
        (7, 1, 7), 
        (0, 5, 0), 
        (15, 3, 5), 
        (1, 2, 0.5), 
    ]) 
    def test_divide_valid(self, a, b, expected): 
        assert self.calc.divide(a, b) == expected 
 
    @pytest.mark.parametrize("a, b", [ 
        (10, 0), 
        (0, 0), 
        (-5, 0), 
        (100, 0), 
    ]) 
    def test_divide_by_zero(self, a, b): 
        with pytest.raises(ValueError, match="Нельзя делить на ноль!"): 
            self.calc.divide(a, b) 

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