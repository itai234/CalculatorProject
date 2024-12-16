
from Exceptions.LogicExceptions import check_if_float, OperatorFactory
from ArithmeticFunctionsEvaluations.OperatorFactory import *
from TestCode.TestExceptions import factory

operator_factory = OperatorFactory()


def fix_long_numbers(equation: list) -> list:
    """
    :param equation: the input is the equation as a list
    :return: it returns the list of (chars) to connect the more than 1 digit numbers
    """
    i = 0
    while i < len(equation) - 1:
        if equation[i].isdigit() and equation[i + 1].isdigit():
            equation[i] = equation[i] + equation[i + 1]
            del equation[i + 1]
        else:
            i += 1
    return equation


def fix_float_numbers(equation: list, precision: int = 100) -> list:
    """
    :param equation:gets the equation
    :return: returns the equation with the float numbers fixed and together, with maximal precision of 100
    """
    i = 0
    if equation[0] == factory.get_floating_point()[0]:
        raise ValueError("Cant Put floating point at the start")
    while i < len(equation) - 1:
        if equation[i] == factory.get_floating_point()[0]:
            if not check_if_float(equation[i - 1]):
                raise ValueError(f"Invalid Floating Point at {i+1}")
        if check_if_float(equation[i]) and equation[i + 1] == factory.get_floating_point()[0]:
            if i+2 >= len(equation):
                raise ValueError("Cannot Put Multiple floating points in one number/ missing parts of the float.")
            if not check_if_float(equation[i]) or not check_if_float(equation[i + 2]):
                raise ValueError("Cannot Put Multiple floating points in one number/ missing parts of the float.")
            number = equation[i] + equation[i + 1] + equation[i + 2]
            del equation[i + 1]
            del equation[i + 1]
            if '.' in number:
                integer_part, decimal_part = number.split('.')
                decimal_part = decimal_part[:precision]
                equation[i] = f'{integer_part}.{decimal_part}'
            else:
                equation[i] = number
        i += 1
    return equation
