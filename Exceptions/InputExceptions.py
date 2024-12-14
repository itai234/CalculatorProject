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


def CheckUnaryMinuses(equation:list) -> list :
    """
    :param equation:
    :return: checks for illegal locations for the unary minus and if there are returns a list explaining the situation
    """
    operators = set(operatorFactory.getOperators())
    errors = []
    i = 0
    while i < len(equation)-1:
        if equation[i] == '-' and equation[i+1] == '-':
            while equation[i] == '-':
                i+=1
            if equation[i] not in operatorFactory.getNumbers() and equation[i] != '(':
                errors.append(f"Illegal end to the Unary minus: {equation[i]}")
            i+=1
        else:
            i+=1
    return errors



def Check1OperandsOperators(equation: list) -> list:
    Operators = operatorFactory.getOneOperandsOperators()
    LeftSideOperators = [op for op in Operators if operatorFactory.getSide(op) == "left"]
    RightSideOperators = [op for op in Operators if operatorFactory.getSide(op) == "right"]
    errors = []
    i = 0
    while i < len(equation):
        if equation[i] in LeftSideOperators:
            temp = equation[i]
            i += 1
            while i < len(equation) and equation[i] == '-':
                i += 1
            if i >= len(equation) or not CheckIfFloat(equation[i]):
                errors.append(f"You can't put '{temp}' before '{equation[i]}'")
        elif equation[i] in RightSideOperators:
            temp = equation[i]
            if i == 0 :
                errors.append(f"You cant put {temp} at the start")
            if not (CheckIfFloat(equation[i-1]) or  equation[i-1] in RightSideOperators):
                errors.append(f"You can't put '{temp}' after '{equation[i - 1]} or before nothing")
        i += 1
    return errors

def CheckIfFloat(word:str)->bool:
    list = operatorFactory.getNumbers()
    list.extend(operatorFactory.getFloatingPoint())
    list.append('-')
    list.append('+')
    for x in word :
        if not x in list:
            return False
    return True

def Check2OperandsOperatorsRightSide(equation: list) -> list:
    Operators = operatorFactory.getTwoOperandsOperators()
    Operators.remove('-')
    Operators.remove('+')
    errors = []
    i = 0
    while i < len(equation):
        if equation[i] in Operators:
            if i == 0 or i == len(equation) - 1:
                errors.append(f"Cannot put the operator '{equation[i]}' at the start or end of the equation")
            elif not CheckIfFloat(equation[i-1]) or  not CheckIfFloat(equation[i+1]):
                if equation[i-1] not in operatorFactory.getClosingParenthesis() and equation[i+1] not in operatorFactory.getOpeningParenthesis():
                     errors.append(f"Operator '{equation[i]}' must be surrounded by valid operands (numbers) or parenthesis")
        i += 1
    return errors

def checkForMissingParenthesis(equation:list)->list :
    """
    :param equation: gets the equation
    :return: checks if the equation is allowed with the right amout of parenthesis and if they are put right.
    """
    OpeningParenthesis = operatorFactory.getOpeningParenthesis()
    ClosingParenthesis = operatorFactory.getClosingParenthesis()
    pairs = operatorFactory.getParenthesisPairs()
    errors = []
    stack = []
    for element in equation:
        if element in OpeningParenthesis:
            stack.append(element)
        if element in ClosingParenthesis:
            if len(stack) == 0 :
                errors.append(f"Invalid connection of Parenthesis :  {element}")
            else:
                poped = stack.pop()
                if pairs.get(poped) != element:
                     errors.append(f"Invalid connection of Parenthesis : {poped} , {element}")
    if len(stack)>0:
        errors.append("The Parenthesis are not Equally split in the equation")
    return errors


