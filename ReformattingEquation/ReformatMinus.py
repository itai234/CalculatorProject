import ArithmeticFunctionsEvaluations.OperatorFactory
from ArithmeticFunctionsEvaluations.OperatorFactory import OperatorFactory


def UnaryMinus(equation:list) -> list:
    """
    :param equation: receives the equation
    :return:  returns the fixed equation with the correct connection of the minuses in the equation(whether its binary or unary and acts as a sign or has priority)
    """
    operators = set(OperatorFactory().getOperators())
    isNeg = False
    i = 0

    while i < len(equation):
        # Check for an operator followed by a minus
        if equation[i] in operators and i + 1 < len(equation) and equation[i + 1] == '-':
            i += 1
            while i < len(equation) and equation[i] == '-':
                isNeg = not isNeg
                del equation[i]
            if i < len(equation) and isNeg:
                equation[i] = '-' + equation[i]
                isNeg = False
        i += 1
    return equation
