from Exceptions.InputExceptions import  *
from Exceptions.EquationValidateException import *
def ValidateEquation(equation: list) -> None:
    """
    gathers a list of the exceptions in the equation and sends it to the customer exception class
    :param
    """
    errors = []
    errors.extend(IsValidLetters(equation))
    errors.extend(IsValidOperators(equation))
    if errors:
        raise EquationValidationError(errors)

