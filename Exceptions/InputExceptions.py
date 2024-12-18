from ArithmeticFunctionsEvaluations.OperatorFactory import *

operatorFactory = OperatorFactory()


def is_valid_letters(equation: list) -> list:
    """
    the function receives the equation and checks if all the equation characters are legal , if it isn't
    it will return all the illegal characters in the equation
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
    the function receives the equation and checks for duplicated operators , besides + and minus that can be duplicated.
    if there are duplicates it will add them to the list of errors and return it in the end.
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
    the function receives the list and checks for missing parenthesis, including the operators without right side
    and operators without left side to not include them in certain checks.
    checks for : () ,( , ) ,
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
            errors.append(f"Empty brackets at position {i+1}, {i + 2}.")
        if element in opening_parenthesis:
            if i > 0 and equation[i - 1] not in operators_without_right_side:
                errors.append(f"Illegal opening parenthesis at position {i+1}.")
            stack.append((element, i))
        elif element in closing_parenthesis:
            if i + 1 < len(equation) and equation[i + 1] not in operators_without_left_side:
                errors.append(f"Illegal closing parenthesis at position {i+1}.")
            if not stack:
                errors.append(f"Unmatched closing '{element}' at position {i+1}.")
            else:
                last_open, open_pos = stack.pop()
                if pairs[last_open] != element:
                    errors.append(f"Mismatched parenthesis: '{last_open}' at position {open_pos} "
                                  f"and '{element}' at position {i+1}.")

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
