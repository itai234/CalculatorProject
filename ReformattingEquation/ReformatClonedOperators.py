from ArithmeticFunctionsEvaluations.Operator import Operator
from ArithmeticFunctionsEvaluations.OperatorFactory import OperatorFactory


def fix_cloned_operators(equation: list) -> list:
    """
    :param equation: the input is the list of the equation(list of chars )
    :return: returns the list without cloned unnecessary operators
    """
    i = 0
    allowed_plus = OperatorFactory().get_closing_parenthesis()
    allowed_plus.extend(OperatorFactory().get_numbers())
    right_operators = OperatorFactory().get_one_operands_operators()
    right_operators = list(set(right_operators)-set(OperatorFactory().get_one_operands_operators_left_side()))
    allowed_plus.extend(right_operators)
    while i < len(equation) - 1:
        if equation[i] == '+':
            if i == 0 or equation[i-1] not in allowed_plus:
                raise ValueError(f"Cannot Put Plus without operators or brackets at location {i+1}")
            if equation[i+1] in OperatorFactory().get_closing_parenthesis():
                raise ValueError(f"Cannot Put Plus and Closing brackets  at  {i+1}")
        if equation[i] in '+' and equation[i] == equation[i + 1]:
            del equation[i+1]
        else:
            i += 1
    return equation

