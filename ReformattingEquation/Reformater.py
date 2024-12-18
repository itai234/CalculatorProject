from Exceptions.ValidateEquation import validate_equation
from ReformattingEquation.ReformatClonedOperators import fix_cloned_operators
from ReformattingEquation.ReformatFloatAndNumber import fix_long_numbers, fix_float_numbers
from ReformattingEquation.ReformatMinus import *
from ReformattingEquation.ReformatSpaces import fix_spaces_in_equation


def reformat(equation: str) -> list:
    """
    this function handles all the reformatting of the equation
    calls all the functions of the reformatting.
    """
    equation = fix_spaces_in_equation(equation)
    equation = list(equation)
    if not equation:
        raise ValueError("Cannot Enter An Empty List")
    equation = fix_cloned_operators(equation)
    equation = fix_long_numbers(equation)
    equation = fix_float_numbers(equation)
    equation = handle_unary_minus(equation)
    equation = handle_sign_minus(equation)
    validate_equation(equation)
    return equation
