
from Exceptions.LogicExceptions import CheckIfFloat, operatorFactory
from ArithmeticFunctionsEvaluations.OperatorFactory import *

operatorFactory = OperatorFactory()

def FixLongNumbers(equation: list) ->list:
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



def FixFloatNumbers(equation:list,precision : int = 100) -> list :
    """
    :param equation:gets the equation
    :return: returns the equation with the float numbers fixed and together, with maximal precision of 100
    """
    i = 0
    if equation[0] == '.':
        raise  ValueError("Cant Put floating point at the start")
    while i < len(equation) - 1:
        if equation[i] == '.':
            if not CheckIfFloat(equation[i-1]):
                raise ValueError(f"Invalid Floating Point at {i+1}")
        if CheckIfFloat(equation[i]) and equation[i + 1] == '.':
            if i+2 >= len(equation):
                raise ValueError("Cannot Put Multiple floating points in one number/ missing parts of the float.")
            if not CheckIfFloat(equation[i]) or not CheckIfFloat(equation[i+2]):
                raise ValueError("Cannot Put Multiple floating points in one number/ missing parts of the float.")
            number = equation[i] + equation[i + 1] + equation[i + 2]
            del equation[i + 1]
            del equation[i + 1]
            if '.' in number:
                integerPart, decimalPart = number.split('.')
                decimalPart = decimalPart[:precision]
                equation[i] = f'{integerPart}.{decimalPart}'
            else:
                equation[i] = number
        i += 1
    return equation
