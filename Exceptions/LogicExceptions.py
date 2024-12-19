
from ArithmeticFunctionsEvaluations.Properties import *



def check_2_operands_operators(equation: list) -> list:
    """
    the function is responsible to check and validate the 2 operands
    operators in the list , if they are surrounded by parenthesis or values
    if an operator is not surrounded by operands or parenthesis or right side operators. it will
    return a list of the errors.
    """
    operators = get_two_operands_operators()
    operators.remove('-')
    right_side_operators = get_one_operands_operators()
    right_side_operators = list(set(right_side_operators)-set(get_one_operands_operators_left_side()))
    errors = []
    i = 0
    while i < len(equation):
        if equation[i] in operators:
            if i == 0 or i == len(equation) - 1:
                errors.append(f"Cannot put the operator '{equation[i]}' at the start or end of the equation")
            elif not check_if_float(equation[i - 1]) or not check_if_float(equation[i + 1]):
                errors = two_operands_false_condition(equation,i,errors,right_side_operators)
        i += 1
    return errors


def two_operands_false_condition(equation:list , i: int , errors:list , right_side_operators: list) -> list:
    """
    the function gets current index, the equation and errors list and searches if the location of the 2 operands operator is legal or not.
    (if it is not near parenthesis or right side operators..)
    """
    if equation[i - 1] not in get_closing_parenthesis() \
            and equation[i + 1] not in get_opening_parenthesis() \
            and equation[i - 1] not in right_side_operators:
        if equation[i + 1] in get_one_operands_operators_left_side():  # removed equation[i] == '+'---
            pass
        else:
            errors.append(f"Operator '{equation[i]}' at location {i + 1} \
            must be surrounded by valid operands (numbers) or parenthesis")
    return errors


def check_1_operands_operators(equation: list) -> list:
    """
    the function checks and validates if the equation is legal by
    checking the 1 operands operators.
    it has multiple checks inside of it.
    """
    operators = get_one_operands_operators()
    left_side_operators = get_one_operands_operators_left_side()
    right_side_operators = get_one_operands_operators_right_side()
    errors = []
    i = 0
    while i < len(equation):
        if equation[i] in left_side_operators:
            errors = handle_1_operands_left_side(equation,i,errors,left_side_operators,right_side_operators)
        elif equation[i] in right_side_operators:
            errors = handle_1_operands_right_side(equation,i,errors,left_side_operators,right_side_operators)
        i += 1
    return errors


def handle_1_operands_right_side(equation: list , i: int , errors : list, left_side_operators: list , right_side_operators: list) -> list:
    """
    the function handles the 1 operands operators, it receives the equation , a certain index , and the operators lists.
    it checks all the legal placements for the right side operators:
    checks situations like 3+! or !3 or ! nad more that are not legal and if it's the case it adds them to the errors list it got.
    so checks for - putting right side operators at the start, putting them with no operators or with left operators like 3!~3,in the start.
    """
    temp = equation[i]
    if i + 1 < len(equation) and (check_if_float(equation[i + 1]) or equation[i + 1] in left_side_operators):
        errors.append(f"You cant put {temp} at this position {i+1} , not enough operators")
    if i == 0:
        errors.append(f"You cant put {temp} at the start")
    if not check_if_float(equation[i - 1]) and equation[i - 1] not in right_side_operators:
        if equation[i - 1] in get_closing_parenthesis():
            pass
        else:
            errors.append(f"You can't put '{temp}' after '{equation[i - 1]} or before nothing at this position {i+1}")
    return errors


def handle_1_operands_left_side(equation: list , i: int , errors : list, left_side_operators: list , right_side_operators: list) -> list:
    """
    the function handles the 1 operands operators, it receives the equation , a certain index , and the operators lists.
    it checks all the legal placements for the left operators:
    checks situations like 3~3 or 3!~3 that are not legal and if it's the case it adds them to the errors list it got.
    it also checks if you put the left side operators at the end or before illegal character that they cannot be before.
    """
    temp = equation[i]
    if i - 1 >= 0 and (check_if_float(equation[i - 1]) or equation[i - 1] in right_side_operators):
        errors.append(f"You cant put {temp} at this position {i}, not enough operators")
    i += 1
    while i < len(equation) and equation[i] == '-':
        i += 1
    if i >= len(equation) or not (check_if_float(equation[i]) or get_opening_parenthesis()[0]):
        if i >= len(equation):
            errors.append(f"You can't put {temp} in the end")
        else:
            errors.append(f"You can't put '{temp}' before '{equation[i]}'")
    return errors


def check_if_float(word: str) -> bool:
    """
    the function checks if the str given to it is a float number.
    """
    valid_chars = get_numbers() + get_floating_point() + list(get_minus())
    if word == get_minus():
        return False
    if word in get_floating_point():
        return False
    return all(char in valid_chars for char in word)


def check_for_invalid_floating_points(equation: list) -> list:
    """
    the function checks for invalid floating points in it for example:
    3.3.3
    and if there are it will add them to the errors list and returns it.
    """
    errors = []
    i = 0
    while i < len(equation):
        element = equation[i]
        if check_if_float(element) or element in get_floating_point():
            num_str = ''
            while i < len(equation) and (check_if_float(equation[i]) or equation[i] in get_floating_point()):
                num_str += equation[i]
                i += 1
            if num_str.count(get_floating_point()[0]) > 1:
                errors.append(f"Invalid float detected: '{num_str}'")
        else:
            i += 1
    return errors


def check_unary_minuses(equation: list) -> list:
    """
    the function receives the equation and check legality for the unary minus ,
    checks if the unary minus is before a closing parenthesis, checks if the character the unary minus is on is legal (numbers or opening parenthesis)
    """
    operators = set(get_operators())
    errors = []
    i = 0
    while i < len(equation) - 1:
        if equation[i] == get_minus() and equation[i+1] in get_closing_parenthesis():
            errors.append("Cannot Enter a minus and a closing parenthesis after it.")
        if equation[i] == get_minus() and equation[i + 1] == get_minus():
            while equation[i] == get_minus():
                i += 1
            if equation[i] not in get_numbers() and equation[i] != get_closing_parenthesis()[0]:
                errors.append(f"Illegal end to the Unary minus: {equation[i]}")
            i += 1
        else:
            i += 1
    return errors
