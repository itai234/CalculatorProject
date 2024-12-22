from ArithmeticFunctionsEvaluations.Properties import *


def fix_cloned_operators(equation: list) -> list:
    """
    receives the equation and checks if it has duplicates of pluses
    it also checks for illegal plus signs in the equation
    and if there are it will raise an exception
    """
    i = 0
    allowed_plus = list(PARENTHESIS[1])
    allowed_plus.extend(list(NUMBERS))
    allowed_plus.extend(list(ONE_OPERAND_OPERATORS_RIGHT))

    while i < len(equation) - 1:
        if equation[i] == '+':
            if i == 0 or equation[i-1] not in allowed_plus:
                raise ValueError(f"Cannot Put Plus without operators or brackets at location {i+1}")
            if equation[i+1] in PARENTHESIS[1]:
                raise ValueError(f"Cannot Put Plus and Closing brackets  at location {i+1}")
        if equation[i] in '+' and equation[i] == equation[i + 1]:
            del equation[i+1]
        else:
            i += 1
    return equation

