import ArithmeticFunctionsEvaluations.OperatorFactory
from ArithmeticFunctionsEvaluations.OperatorFactory import OperatorFactory


def IsValidLetters(equation: list) -> list:
    """
    :param list:  gets the equation  and checks if the equation is valid(in the prespective of letters)
    :return: returns true if the list is valid and else raises an error
    """
    allowedLetters = set("0123456789(). ")
    allowedOperators = set(OperatorFactory().getOperators())  # Ensure to call getOperators to get a list
    allowedLetters.update(allowedOperators)  # Update the set with allowed operators

    errors = []

    if not equation or all(char == " " for char in equation):
        errors.append("The equation is either empty or contains only spaces.")
    for char in equation:
        if char not in allowedLetters:
            errors.append(f"Illegal character in the equation : {char} ")
    return errors

def IsValidOperators(equation:list) -> list:
    errors = []
    IllegalDuplication = set(OperatorFactory().getOperators())
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


