
import ArithmeticFunctionsEvaluations.OperatorFactory
from ArithmeticFunctionsEvaluations.OperatorFactory import OperatorFactory
from Exceptions.InputExceptions import operatorFactory

factory = OperatorFactory()




def handle_unary_minus(equation: list) -> list:
    """
    Handles unary minus by transforming double minuses into a positive sign.
    If only one minus is found, it remains as is.
    :param equation: List representation of the equation.
    :return: The equation with unary minus correctly handled.
    """
    i = 0
    while i < len(equation)-1:
        # Check for consecutive minuses, e.g., "--" case
        if equation[i] == '-' and i + 1 < len(equation) and equation[i + 1] == '-' and i == 0:
            del equation[i]
            del equation[i]
            if equation[i] not in factory.getOpeningParenthesis() and not checkIfAllLegalChars(equation[i]) and equation[i]!='-':
                raise ValueError("The Expression Is Invalid because Unary minus can only be besides brackets,numbers or other minuses")
            continue

        i += 1
    return equation


def handle_sign_minus(equation: list) -> list:
    """
    """
    operators = factory.getOperators()
    operators.remove('!')
    operators.remove('#')
    #operators.remove('-')
    i = 0
    while i < len(equation) - 1:
        if equation[i] in operators and i + 1 < len(equation) and equation[i + 1] == '-' and (i!=0 or equation!='-'):
            IsMinus = False
            while equation[i + 1 ] == '-':
                IsMinus= not IsMinus
                del equation[i+1]
            if checkIfAllLegalChars(equation[i+1]) or equation[i+1] in operatorFactory.getOpeningParenthesis():
               if IsMinus:
                   if checkIfAllLegalChars(equation[i+1]) :
                       equation[i + 1] = '-' + equation[i + 1]
                   if equation[i+1] in operatorFactory.getOpeningParenthesis():
                        equation = InsertMinusAndParenthesis(equation,i+1)
            else:
                raise ValueError("cannot put minus sign on non numbers")
        else:
            i += 1
    return equation


def checkIfAllLegalChars(equation: str) -> bool:
    """
    Validates if all characters in the equation are legal for operands.

    :param equation: A string representing part of the equation.
    :return: True if all characters are legal, False otherwise.
    """
    legalChars = factory.getNumbers() + factory.getFloatingPoint() + ['-']
    return all(char in legalChars for char in equation)



def InsertMinusAndParenthesis(equation:list,index:int) ->list:

    equation.insert(index,operatorFactory.getOpeningParenthesis()[0])
    equation.insert(index+1, '-')
    count = 0
    index+=2
    while index< len(equation):
        if(equation[index] in operatorFactory.getOpeningParenthesis()):
            count+=1
        if(equation[index] in operatorFactory.getClosingParenthesis()):
            count-=1
        if count == 0 :
            equation.insert(index+1,operatorFactory.getClosingParenthesis()[0])
            return equation
        index+=1
    return equation



