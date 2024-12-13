import ArithmeticFunctionsEvaluations.OperatorFactory
from ArithmeticFunctionsEvaluations.OperatorFactory import OperatorFactory


def UnaryMinus(equation:list) -> list:
    """
    :param equation: receives the equation
    :return:  returns the fixed equation with the correct connection of the minuses in the equation(whether its binary or unary and acts as a sign or has priority)
    """
    operators = set(OperatorFactory().getOperators())
    isUnaryMinus = False
    i = 0

    while i < len(equation):
        # Check for an operator followed by a minus
        if equation[i] in operators and i + 1 < len(equation) and equation[i + 1] == '-':
            i += 1
            while i < len(equation) and equation[i] == '-':
                isUnaryMinus = not isUnaryMinus
                del equation[i]  # Remove the current minus
            if i < len(equation) and isUnaryMinus:
                if not (equation[i] in OperatorFactory().getNumbers() or  equation[i] in OperatorFactory().getOpeningParenthesis()):
                    raise ValueError("Illegal unary minus!")
                else:
                    equation[i] = '-' + equation[i]  # Attach the unary minus
                    isUnaryMinus = False
        i += 1
    return equation
