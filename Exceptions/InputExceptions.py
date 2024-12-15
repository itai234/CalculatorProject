from ArithmeticFunctionsEvaluations.OperatorFactory import *

operatorFactory = OperatorFactory()


def IsValidLetters(equation: list) -> list:
    """
    :param list:  gets the equation  and checks if the equation is valid(in the prespective of letters)
    :return: returns true if the list is valid and else raises an error
    """
    allowedLetters = set(operatorFactory.getAllLegalLetters())
    errors = []

    if not equation or all(char == " " for char in equation):
        errors.append("The equation is either empty or contains only spaces.")
    for x in equation:
        for char  in x:
            if char not in allowedLetters:
                 errors.append(f"Illegal character in the equation : {char} ")
    return errors

def IsValidOperators(equation:list) -> list:
    """
    :param equation: gets the equation as a list
    :return: checks for errors of duplicated operators that are illegal to dup and if there are return a list of errors containing them
    """
    errors = []
    IllegalDuplication = set(operatorFactory.getOperators())
    IllegalDuplication.remove('+')
    IllegalDuplication.remove('-')
    IllegalDuplication.remove('#')
    IllegalDuplication.remove('!')
    i = 0
    while i < len(equation) -1:
        if equation[i] in IllegalDuplication and equation[i+1] == equation[i]:
            errors.append(f"Cannot Duplicate this type of Operator: {equation[i]}")
            equation = [item for item in equation if item!= equation[i]]
        else:
            i+=1
    return errors


def checkForMissingParenthesis(equation: list) -> list:
    """
    Checks for balanced and correctly matched parentheses in the equation.
    :param equation: The input equation as a list of tokens.
    :return: A list of error messages.
    """
    OpeningParenthesis = operatorFactory.getOpeningParenthesis()
    ClosingParenthesis = operatorFactory.getClosingParenthesis()
    operatorsWithoutRightSide = operatorFactory.getOperators()
    operatorsWithoutRightSide.remove("#")
    operatorsWithoutRightSide.remove("!")
    operatorsWithoutLeftSide = operatorFactory.getOperators()
    operatorsWithoutLeftSide.remove("~")
    pairs = operatorFactory.getParenthesisPairs()
    stack, errors = [], []
    for i, element in enumerate(equation):
        if equation[i] in OpeningParenthesis and equation[i+1] in ClosingParenthesis:
            errors.append(f"empty Brackets at position {i},{i+1}.")
        if element in OpeningParenthesis:
            if i!=0 and equation[i-1] not in operatorsWithoutRightSide:
                errors.append(f"Illegal Parenthesis in position{i}")
            stack.append(element)
        elif element in ClosingParenthesis:
            if i+1!=len(equation) and equation[i+1] not in operatorsWithoutLeftSide:
                errors.append(f"Illegal Parenthesis in position {i}")
            if not stack:
                errors.append(f"Unmatched closing '{element}' at position {i}.")
            elif pairs[stack.pop()] != element:
                errors.append(f"Mismatched parenthesis at position {i}.")
    if stack:
        errors.append("Unmatched opening parentheses remain.")

    return errors

def checkEndOfEquation(equation:list)->list:
    errors =[]
    if equation[-1] in "+-":
        errors.append(f"Cannot End The Equation With {equation[-1]}")
    return errors


