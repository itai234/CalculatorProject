from Exceptions.InputExceptions import  *
from Exceptions.EquationValidateException import *
from Exceptions.LogicExceptions import *
def ValidateEquation(equation: list) -> None:
    """
    gathers a list of the exceptions in the equation and sends it to the customer exception class
    :param
    """
    errors = []
    errors.extend(IsValidLetters(equation))
    errors.extend(IsValidOperators(equation))
    errors.extend(CheckUnaryMinuses(equation))
    errors.extend(Check1OperandsOperators(equation))
    errors.extend(Check2OperandsOperatorsRightSide(equation))
    errors.extend(checkForMissingParenthesis(equation))
    errors.extend(checkEndOfEquation(equation))
    errors.extend(checkForInvalidFloatingPoints(equation))
    if errors:
        raise EquationValidationError(errors)

