
from ArithmeticFunctionsEvaluations.OperatorFactory import *
from TestCode.TestArithmeticFunctions import factory

operatorFactory = OperatorFactory()


def check_2_operands_operators_right_side(equation: list) -> list:
    """
    the function is responsible to check and validate the 2 operands
    operators in the list , if they are surrounded by parenthesis or values
    """
    operators = operatorFactory.get_two_operands_operators()
    operators.remove('-')
    right_side_operators = operatorFactory.get_one_operands_operators()
    right_side_operators = list(set(right_side_operators)-set(operatorFactory.get_one_operands_operators_left_side()))
    errors = []
    i = 0
    while i < len(equation):
        if equation[i] in operators:
            if i == 0 or i == len(equation) - 1:
                errors.append(f"Cannot put the operator '{equation[i]}' at the start or end of the equation")
            elif not check_if_float(equation[i - 1]) or not check_if_float(equation[i + 1]):
                if equation[i - 1] not in operatorFactory.get_closing_parenthesis() \
                        and equation[i + 1] \
                        not in operatorFactory.get_opening_parenthesis() \
                        and equation[i - 1] not in right_side_operators:
                    if equation[i] == '+' or equation[i+1] in operatorFactory.get_one_operands_operators_left_side():
                        pass
                    else:
                        errors.append(f"Operator '{equation[i]}' \
                        must be surrounded by valid operands (numbers) or parenthesis")
        i += 1
    return errors


def check_1_operands_operators(equation: list) -> list:
    """
    the function checks and validates if the equation is legal by
    checking the 1 operands operators.
    """
    operators = operatorFactory.get_one_operands_operators()
    left_side_operators = operatorFactory.get_one_operands_operators_left_side()
    right_side_operators = operatorFactory.get_one_operands_operators_right_side()
    errors = []
    i = 0
    while i < len(equation):
        if equation[i] in left_side_operators:
            temp = equation[i]
            if i - 1 >= 0 and (check_if_float(equation[i - 1]) or equation[i - 1] in right_side_operators):
                errors.append(f"You cant put {temp} at this position , not enough operators")
            i += 1
            while i < len(equation) and equation[i] == '-':
                i += 1
            if i >= len(equation) or not (check_if_float(equation[i]) or operatorFactory.get_opening_parenthesis()[0]):
                if i >= len(equation):
                    errors.append(f"You can't put {temp} in the end")
                else:
                    errors.append(f"You can't put '{temp}' before '{equation[i]}'")
        elif equation[i] in right_side_operators:
            temp = equation[i]
            if i + 1 < len(equation) and (check_if_float(equation[i + 1]) or equation[i + 1] in left_side_operators):
                errors.append(f"You cant put {temp} at this position , not enough operators")
            if i == 0:
                errors.append(f"You cant put {temp} at the start")
            if not check_if_float(equation[i - 1]) and equation[i - 1] not in right_side_operators:
                if equation[i - 1] in factory.get_closing_parenthesis():
                    pass
                else:
                    errors.append(f"You can't put '{temp}' after '{equation[i - 1]} or before nothing")
        i += 1
    return errors


def check_if_float(word: str) -> bool:
    """
    the function checks if the str given to it is a float number
    """
    valid_chars = operatorFactory.get_numbers() + operatorFactory.get_floating_point() + list(operatorFactory.get_minus())
    if word == operatorFactory.get_minus():
        return False
    if word in factory.get_floating_point():
        return False
    return all(char in valid_chars for char in word)


def check_for_invalid_floating_points(equation: list) -> list:
    """
    the function checks for invalid floating points in it for example:
    3.3.3
    """
    errors = []
    i = 0
    while i < len(equation):
        element = equation[i]
        if check_if_float(element) or element in factory.get_floating_point():
            num_str = ''
            while i < len(equation) and (check_if_float(equation[i]) or equation[i] in factory.get_floating_point()):
                num_str += equation[i]
                i += 1
            if num_str.count(factory.get_floating_point()[0]) > 1:
                errors.append(f"Invalid float detected: '{num_str}'")
        else:
            i += 1
    return errors


def check_unary_minuses(equation: list) -> list:
    """
    :param equation:
    :return: checks for illegal locations for the unary minus and if there are returns a list explaining the situation
    """
    operators = set(operatorFactory.get_operators())
    errors = []
    i = 0
    while i < len(equation) - 1:
        if equation[i] == factory.get_minus() and equation[i+1] in factory.get_closing_parenthesis():
            errors.append("Cannot Enter a minus and a closing parenthesis after it.")
        if equation[i] == factory.get_minus() and equation[i + 1] == factory.get_minus():
            while equation[i] == factory.get_minus():
                i += 1
            if equation[i] not in operatorFactory.get_numbers() and equation[i] != factory.get_closing_parenthesis()[0]:
                errors.append(f"Illegal end to the Unary minus: {equation[i]}")
            i += 1
        else:
            i += 1
    return errors
