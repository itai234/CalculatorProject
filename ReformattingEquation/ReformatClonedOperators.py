from ArithmeticFunctionsEvaluations.Properties import *


def fix_cloned_operators(equation: list) -> list:
    """
    receives the equation and checks if it has duplicates of pluses
    it also checks for illegal plus signs in the equation
    and if there are it will raise an exception
    """
    i = 0
    allowed_plus = get_closing_parenthesis()
    allowed_plus.extend(get_numbers())
    right_operators =get_one_operands_operators()
    right_operators = list(set(right_operators)-set(get_one_operands_operators_left_side()))
    allowed_plus.extend(right_operators)
    while i < len(equation) - 1:
        if equation[i] == '+':
            if i == 0 or equation[i-1] not in allowed_plus:
                raise ValueError(f"Cannot Put Plus without operators or brackets at location {i+1}")
            if equation[i+1] in get_closing_parenthesis():
                raise ValueError(f"Cannot Put Plus and Closing brackets  at location {i+1}")
        if equation[i] in '+' and equation[i] == equation[i + 1]:
            del equation[i+1]
        else:
            i += 1
    return equation

