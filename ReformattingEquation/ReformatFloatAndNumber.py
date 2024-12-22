
from ArithmeticFunctionsEvaluations.Properties import *
from Exceptions.LogicExceptions import check_if_float


def fix_long_numbers(equation: list) -> list:
    """
    the function gets the equation and if an element in the equation is a single number it will connect it to the rest the number
    example  - 2,3,4 = 234 , 0234 = 234
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
    the function receives the equation and checks for floating points to connect -
    example - 3123,., 123 = 3123.123
    if it finds mistakes like floating point at the start of the equation or floating point on non numbers
    or putting multiple floating points it will raise an error else it will build the number
    """
    i = 0
    if equation[0] == FLOATING_POINT[0]:
        raise ValueError("Cant Put floating point at the start")
    while i < len(equation) - 1:
        if equation[i] == FLOATING_POINT[0]:
            if not check_if_float(equation[i - 1]):
                raise ValueError(f"Invalid Floating Point at {i+1}")
        if check_if_float(equation[i]) and equation[i + 1] == FLOATING_POINT[0]:
            equation = fix_float_numbers_handler(equation,i, precision)
        i += 1
    return equation


def fix_float_numbers_handler(equation:list , i: int, precision: int) -> list:
    """
    the function handles the replacing of the dot and connecting the float number itself.
    this is a helper function for fix_float_numbers.
    """
    if i + 2 >= len(equation):
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
    return equation


