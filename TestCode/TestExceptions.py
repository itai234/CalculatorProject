from ArithmeticFunctionsEvaluations.OperatorFactory import OperatorFactory
from Exceptions.InputExceptions import *
import pytest
factory = OperatorFactory()


def test_side():
    expected = ['~']
    result = Check1OperandsOperators([])
    assert result == expected, f"Test failed: expected {expected}, got {result}"
    print("test_side passed!")