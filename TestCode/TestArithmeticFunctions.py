import  pytest

from ArithmeticFunctionsEvaluations.OperatorFactory import OperatorFactory

factory = OperatorFactory()

def test_FactoryAdd():
    assert factory.Operation('+',2,4)==6

def test_FactorySub():
    assert factory.Operation('-',3,4)==-1

def test_FactoryMul():
    assert factory.Operation('*',3,4)==12

def test_FactoryDiv():
    assert factory.Operation('/',3,4)==0.75

def test_FactoryPow():
    assert factory.Operation('^',3,4)==81

def test_FactoryMod():
    assert factory.Operation('%',3,0)==0

def test_FactoryMax():
    assert factory.Operation('$',3,4)==4

def test_FactoryMin():
    assert factory.Operation('&',3,4)==3

def test_FactoryAvg():
    assert factory.Operation('@',3,4)==3.5

def test_FactoryNeg():
    assert factory.Operation('~',32)==-32

def test_FactoryFactorial():
    assert factory.Operation('!',3,)==6










