from ArithmeticFunctionsEvaluations.Operator import Operator
from ArithmeticFunctionsEvaluations.OperatorFactory import OperatorFactory


def FixClonedOperators(equation:list) -> list :
    """
    :param equation: the input is the list of the equation(list of chars )
    :return: returns the list without cloned unnecessary operators
    """
    i = 0
    allowedPlus = OperatorFactory().getClosingParenthesis()
    allowedPlus.extend(OperatorFactory().getNumbers())
    rightOperators  =  OperatorFactory().getOneOperandsOperators()
    rightOperators.remove("~")
    allowedPlus.extend(rightOperators)
    while i < len(equation) - 1:
        if equation[i] == '+':
            if i==0 or equation[i-1] not in allowedPlus:
                raise ValueError(f"Cannot Put Plus without operators or brackets at location {i+1}")
        if equation[i] in "+" and equation[i] == equation[i + 1]:
            del equation[i+1]
        else:
            i += 1
    return equation

