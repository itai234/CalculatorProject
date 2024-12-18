from Exceptions.InputExceptions import *
from Exceptions.EquationValidateException import *
from Exceptions.LogicExceptions import *


def validate_equation(equation: list) -> None:
    """
    gathers a list of the exceptions in the equation and sends it to the customer exception class,
    if there are errors at least one it will send them to the custom class of exceptions, and it will print out a list of all
    the exceptions
    :param
    """
    errors = []
    errors.extend(is_valid_letters(equation))
    errors.extend(is_valid_operators(equation))
    errors.extend(check_unary_minuses(equation))
    errors.extend(check_1_operands_operators(equation))
    errors.extend(check_2_operands_operators(equation))
    errors.extend(check_for_missing_parenthesis(equation))
    errors.extend(check_end_of_equation(equation))
    errors.extend(check_for_invalid_floating_points(equation))
    if errors:
        raise EquationValidationError(errors)

