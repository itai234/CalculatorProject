from ArithmeticFunctionsEvaluations.Properties import *

def is_valid_letters(equation: list) -> list:
    """
    the function receives the equation and checks if all the equation characters are legal , if it isn't
    it will return all the illegal characters in the equation
    """
    allowed_letters = set(get_all_legal_letters())
    errors = []

    for char in ''.join(equation):
        if char not in allowed_letters:
            errors.append(f"Illegal character in the equation: {char}")
    return errors


def check_for_missing_parenthesis(equation: list) -> list:
    """
    the function receives the list and checks for missing parenthesis, including the operators without right side
    and operators without left side to not include them in certain checks.
    checks for : () ,( , ) ,
    """
    opening_parenthesis = get_opening_parenthesis()
    closing_parenthesis = get_closing_parenthesis()
    operators_without_right_side = get_operators().copy()

    operators_without_right_side = list(set(operators_without_right_side)\
                                        -set(get_one_operands_operators_right_side()))
    operators_without_right_side.extend(opening_parenthesis)
    operators_without_left_side = get_operators().copy()
    operators_without_left_side = list(set(operators_without_left_side)\
                                       - set(get_one_operands_operators_left_side()))
    operators_without_left_side.extend(closing_parenthesis)
    pairs = get_parenthesis_pairs()
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
            errors,stack = check_missing_parenthesis_after_closing_parenthesis(equation,i,errors,stack,element,operators_without_left_side)

    errors = empty_stack(stack,errors)
    return errors


def check_missing_parenthesis_after_closing_parenthesis(equation: list, i: int, errors:list, stack:list,element:str,operators_without_left_side:list):
    """
    the function handles finding missing parenthesis when receiving a closing parenthesis.
    this is a helper function for : check_for_missing_parenthesis
    """
    pairs = get_parenthesis_pairs()
    if i + 1 < len(equation) and equation[i + 1] not in operators_without_left_side:
        errors.append(f"Illegal closing parenthesis at position {i + 1}.")
    if not stack:
        errors.append(f"Unmatched closing '{element}' at position {i + 1}.")
    else:
        last_open, open_pos = stack.pop()
        if pairs[last_open] != element:
            errors.append(f"Mismatched parenthesis: '{last_open}' at position {open_pos} "
                          f"and '{element}' at position {i + 1}.")

    return errors,stack


def empty_stack(stack: list , errors: list) -> list:
    """
    the function empties a stack, and if there are elements in the stack it will append to the errors list the elements.
    this is a helper function for : check_for_missing_parenthesis
    """
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
