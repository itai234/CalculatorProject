import ArithmeticFunctionsEvaluations.OperatorFactory
from ArithmeticFunctionsEvaluations.OperatorFactory import OperatorFactory
factory = OperatorFactory()


def UnaryMinus(equation:list) -> list:
    """
    :param equation: receives the equation
    :return:  returns the fixed equation with the correct connection of the minuses in the equation(whether its binary or unary and acts as a sign or has priority)
    """
    operators = set(OperatorFactory().getOperators())
    operators.remove('!')
    operators.remove('#')
    isUnaryMinus = False
    i = 0

    while i < len(equation):
        didJump = False
        # Check for an operator followed by a minus
        if equation[i] in operators and i + 1 < len(equation) and equation[i + 1] == '-' :#and (checkIfAllLegalChars(equation[i+2]) or equation[i+2] == factory.getOpeningParenthesis()) :
            i += 1
            didJump = False
            while i < len(equation) and equation[i] == '-':
                isUnaryMinus = not isUnaryMinus
                del equation[i]  # Remove the current minus
            if i < len(equation) and isUnaryMinus:
                if not (checkIfAllLegalChars(equation[i]) or  equation[i] in factory.getOpeningParenthesis()):
                    raise ValueError("Illegal unary minus!")
                else:
                    if equation[i] in factory.getOpeningParenthesis():
                        if equation[i] == '-' and equation[i-2] == '-':
                            del[equation[i-1]]
                            didJump = True
                    else:
                        equation[i] = '-' + equation[i]  # Attach the unary minus
                    isUnaryMinus = False
        if didJump == False:
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
