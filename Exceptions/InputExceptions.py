from ArithmeticFunctionsEvaluations.OperatorFactory import *

operatorFactory = OperatorFactory()


def is_valid_letters(equation: list) -> list:
    """
    :param list:  gets the equation  and checks if the equation is valid(in the prespective of letters)
    :return: returns true if the list is valid and else raises an error
    """
    allowed_letters = set(operatorFactory.get_all_legal_letters())
    errors = []

    if not equation or all(char == " " for char in equation):
        errors.append("The equation is either empty or contains only spaces.")
    for x in equation:
        for char in x:
            if char not in allowed_letters:
                errors.append(f"Illegal character in the equation : {char} ")
    return errors


def is_valid_operators(equation: list) -> list:
    """
    :param equation: gets the equation as a list
    :return: checks for errors of duplicated operators that are illegal to dup and if there are return a list of errors containing them
    """
    errors = []
    illegal_duplication = set(operatorFactory.get_operators())
    illegal_duplication.remove('+')
    illegal_duplication.remove('-')
    illegal_duplication = list(set(illegal_duplication) - set(operatorFactory.get_one_operands_operators_right_side()))
    i = 0
    while i < len(equation) - 1:
        if equation[i] in illegal_duplication and equation[i + 1] == equation[i]:
            errors.append(f"Cannot Duplicate this type of Operator: {equation[i]}")
            equation = [item for item in equation if item != equation[i]]
        else:
            i += 1
    return errors


def check_for_missing_parenthesis(equation: list) -> list:
    """
    Checks for balanced and correctly matched parentheses in the equation.
    :param equation: The input equation as a list of the equation.
    :return: A list of error messages (if there are).
    """
    opening_parenthesis = operatorFactory.get_opening_parenthesis()
    closing_parenthesis = operatorFactory.get_closing_parenthesis()
    operators_without_right_side = operatorFactory.get_operators().copy()

    operators_without_right_side = list(set(operators_without_right_side)\
                                        -set(operatorFactory.get_one_operands_operators_right_side()))
    operators_without_right_side.extend(opening_parenthesis)
    operators_without_left_side = operatorFactory.get_operators().copy()
    operators_without_left_side = list(set(operators_without_left_side)\
                                       - set(operatorFactory.get_one_operands_operators_left_side()))
    operators_without_left_side.extend(closing_parenthesis)
    pairs = operatorFactory.get_parenthesis_pairs()
    stack = []
    errors = []

    for i, element in enumerate(equation):
        if element in opening_parenthesis and i + 1 < len(equation) and equation[i + 1] in closing_parenthesis:
            errors.append(f"Empty brackets at position {i}, {i + 1}.")
        if element in opening_parenthesis:
            if i > 0 and equation[i - 1] not in operators_without_right_side:
                errors.append(f"Illegal opening parenthesis at position {i}.")
            stack.append((element, i))
        elif element in closing_parenthesis:
            if i + 1 < len(equation) and equation[i + 1] not in operators_without_left_side:
                errors.append(f"Illegal closing parenthesis at position {i}.")
            if not stack:
                errors.append(f"Unmatched closing '{element}' at position {i}.")
            else:
                last_open, open_pos = stack.pop()
                if pairs[last_open] != element:
                    errors.append(f"Mismatched parenthesis: '{last_open}' at position {open_pos} "
                                  f"and '{element}' at position {i}.")

    while stack:
        unmatched_open, pos = stack.pop()
        errors.append(f"Unmatched opening '{unmatched_open}' at position {pos}.")

    return errors


def check_end_of_equation(equation: list) -> list:
    """
    checks the end of the equation if a plus or a minus and if it is adds it to
    the error list .
    """
    errors = []
    if equation[-1] in "+-":
        errors.append(f"Cannot End The Equation With {equation[-1]}")
    return errors
