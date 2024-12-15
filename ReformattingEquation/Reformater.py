from Exceptions.ValidateEquation import ValidateEquation
from ReformattingEquation.ReformatClonedOperators import FixClonedOperators
from ReformattingEquation.ReformatFloatAndNumber import FixLongNumbers, FixFloatNumbers
from ReformattingEquation.ReformatMinus import *
from ReformattingEquation.ReformatSpaces import FixSpacesInEquation


def Reformat(equation: str)-> list:
    equation = FixSpacesInEquation(equation)
    equation = list(equation)
    if not equation:
        raise ValueError("Cannot Enter An Empty List")
    equation = FixClonedOperators(equation)
    equation = FixLongNumbers(equation)
    equation = FixFloatNumbers(equation)
    equation = handle_unary_minus(equation)
    equation = handle_sign_minus(equation)
    ValidateEquation(equation)
    return equation