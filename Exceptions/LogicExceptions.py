from ArithmeticFunctionsEvaluations.OperatorFactory import *
operatorFactory = OperatorFactory()

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
            if  CheckIfFloat(equation[i-1]) == False and  equation[i-1] not in RightSideOperators:
                errors.append(f"You can't put '{temp}' after '{equation[i - 1]} or before nothing")
        i += 1
    return errors


def CheckIfFloat(word:str)->bool:
    valid_chars = operatorFactory.getNumbers() + operatorFactory.getFloatingPoint() + ['-']
    if word == '-':
        return False
    return all(char in valid_chars for char in word)


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

