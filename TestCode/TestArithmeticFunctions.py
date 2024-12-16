import  pytest

from ArithmeticFunctionsEvaluations.OperatorFactory import OperatorFactory

factory = OperatorFactory()

def test_FactoryAdd():
    assert factory.operation('+', 2, 4) == 6

def test_FactorySub():
    assert factory.operation('-', 3, 4) == -1

def test_FactoryMul():
    assert factory.operation('*', 3, 4) == 12

def test_FactoryDiv():
    assert factory.operation('/', 3, 4) == 0.75

def test_FactoryPow():
    assert factory.operation('^', 3, 4) == 81

def test_FactoryMod():
    assert factory.operation('%', 3, 0) == 0

def test_FactoryMax():
    assert factory.operation('$', 3, 4) == 4

def test_FactoryMin():
    assert factory.operation('&', 3, 4) == 3

def test_FactoryAvg():
    assert factory.operation('@', 3, 4) == 3.5

def test_FactoryNeg():
    assert factory.operation('~', 32) == -32

def test_FactoryFactorial():
    assert factory.operation('!', 3) == 6

def test_SumDigits():
    assert factory.operation('#', 123) == 6










