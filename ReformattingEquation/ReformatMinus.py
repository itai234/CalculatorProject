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
    while i < len(equation) - 1:
        # Check for consecutive minuses, e.g., "--" case
        if equation[i] == factory.get_minus() and i + 1 < len(equation) and equation[i + 1] == factory.get_minus() and i == 0:
            del equation[i]
            del equation[i]
            if equation[i] not in factory.get_opening_parenthesis() and not check_if_all_legal_chars(equation[i]) and \
                    equation[i] != '-':
                raise ValueError(
                    "The Expression Is Invalid because Unary minus can only be besides brackets,numbers or other "
                    "minuses")
            continue

        i += 1
    return equation


def handle_sign_minus(equation: list) -> list:
    """
    """
    operators = factory.get_operators()
    operators = list(set(operators) - set(factory.get_one_operands_operators_right_side()))
    i = 0
    while i < len(equation) - 1:
        if equation[i] in operators and i + 1 < len(equation) and equation[i + 1] == factory.get_minus() and (
                i != 0 or equation != factory.get_minus()):
            is_minus = False

            if i + 1 >= len(equation):
                raise ValueError("Wrong placement for minus in the end.")
            while equation[i + 1] == factory.get_minus():
                is_minus = not is_minus
                del equation[i + 1]
                if i + 1 >= len(equation):
                    raise ValueError("Wrong placement for minus in the end.")
            if check_if_all_legal_chars(equation[i + 1]) or equation[i + 1] in operatorFactory.get_opening_parenthesis():
                if is_minus:
                    if check_if_all_legal_chars(equation[i + 1]):
                        equation[i + 1] = factory.get_minus() + equation[i + 1]
                    if equation[i + 1] in operatorFactory.get_opening_parenthesis():
                        equation = insert_minus_and_parenthesis(equation, i + 1)
            else:
                raise ValueError("cannot put minus sign on non numbers")
        else:
            i += 1
    return equation


def check_if_all_legal_chars(equation: str) -> bool:
    """
    Validates if all characters in the equation are legal for operands.

    :param equation: A string representing part of the equation.
    :return: True if all characters are legal, False otherwise.
    """
    legal_chars = factory.get_numbers() + factory.get_floating_point() + list(factory.get_minus())
    return all(char in legal_chars for char in equation)


def insert_minus_and_parenthesis(equation: list, index: int) -> list:
    equation.insert(index, operatorFactory.get_opening_parenthesis()[0])
    equation.insert(index + 1, factory.get_minus())
    count = 0
    index += 2
    while index < len(equation):
        if equation[index] in operatorFactory.get_opening_parenthesis():
            count += 1
        if equation[index] in operatorFactory.get_closing_parenthesis():
            count -= 1
        if count == 0:
            equation.insert(index + 1, operatorFactory.get_closing_parenthesis()[0])
            return equation
        index += 1
    return equation
