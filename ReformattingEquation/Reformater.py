from Exceptions.ValidateEquation import ValidateEquation
from ReformattingEquation.ReformatClonedOperators import FixClonedOperators
from ReformattingEquation.ReformatFloatAndNumber import FixLongNumbers, FixFloatNumbers
from ReformattingEquation.ReformatMinus import UnaryMinus
from ReformattingEquation.ReformatSpaces import FixSpacesInEquation


def Reformat(equation: str)-> list:
    equation = FixSpacesInEquation(equation)
    equation = list(equation)
    equation = FixClonedOperators(equation)
    equation = FixLongNumbers(equation)
    equation = FixFloatNumbers(equation)
    equation = UnaryMinus(equation)
    ValidateEquation(equation)
    return equation