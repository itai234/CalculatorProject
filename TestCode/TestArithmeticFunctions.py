import  pytest

from ArithmeticFunctions import ArithmeticCalculations

calc = ArithmeticCalculations()

def test_add_numbers():
    assert calc.AddNumbers(3, 5) == 8
    assert calc.AddNumbers(-3, 5) == 2

def test_NegNumber():
    assert calc.NegNumber(5) == -5

