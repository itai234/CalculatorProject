import ArithmeticFunctionsEvaluations.OperatorFactory
from ArithmeticFunctionsEvaluations.OperatorFactory import OperatorFactory
from ArithmeticFunctionsEvaluations.Properties import *

def handle_unary_minus(equation: list) -> list:
    """
    handles unary minus by deleting or -
    if only one minus is found, it remains as is, or the that the result of the minues
    should be a one minus.
    the function also checks if there is a illegal unary minus and if there is it will raise an error
    """
    i = 0
    while i < len(equation) - 1:
        # Check for consecutive minuses, e.g., "--" case
        if equation[i] == get_minus() and i + 1 < len(equation) and equation[i + 1] == get_minus() and i == 0:
            del equation[i]
            del equation[i]
            if len(equation) == 0:
                raise ValueError("Cannot enter an Empty Equation")
            if equation[i] not in get_opening_parenthesis() and not check_if_all_legal_chars(equation[i]) and \
                    equation[i] != '-':
                raise ValueError(
                    "The Expression Is Invalid because Unary minus can only be besides brackets,numbers or other "
                    "minuses")
            continue

        i += 1
    return equation

def handle_sign_minus(equation: list) -> list:
    """
    the function handles the sign minus , means that if there is a sign minus it would
    stick to an operand , or if there are parenthesis , it will create a new
    pair of parenthesis with minus in them. -- > (-(5+1))
    the function also search for wrong placements of the minus for example in the end
    or on non numbers
    """
    operators = get_operators()
    operators = list(set(operators) - set(get_one_operands_operators_right_side()))
    i = 0
    while i < len(equation) - 1:
        if equation[i] in operators and i + 1 < len(equation) and equation[i + 1] == get_minus() and (
                i != 0 or equation != get_minus()):
            is_minus = False

            if i + 1 >= len(equation):
                raise ValueError("Wrong placement for minus in the end.")
            while equation[i + 1] == get_minus():
                is_minus = not is_minus
                del equation[i + 1]
                if i + 1 >= len(equation):
                    raise ValueError("Wrong placement for minus in the end.")
            if check_if_all_legal_chars(equation[i + 1]) or equation[i + 1] in get_opening_parenthesis():
                if is_minus:
                    if check_if_all_legal_chars(equation[i + 1]):
                        equation[i + 1] = get_minus() + equation[i + 1]
                    if equation[i + 1] in get_opening_parenthesis():
                        equation = insert_minus_and_parenthesis(equation, i + 1)
            else:
                raise ValueError(f"cannot put minus sign on non numbers, here its on {equation[i+1]} at location {i+1}")
        else:
            i += 1
    return equation


def check_if_all_legal_chars(equation: str) -> bool:
    """
    validates if the given str is a number or not.
    """
    legal_chars = get_numbers() +get_floating_point() + list(get_minus())
    return all(char in legal_chars for char in equation)


def insert_minus_and_parenthesis(equation: list, index: int) -> list:
    """
    this function creates a new pair of parenthesis with minus insides them and inserts
    them between a sub equation, it also will make sure if there are parenthesis with a right side operator outside of them
    to include it , for example 10--(5+3)!
    """
    equation.insert(index, get_opening_parenthesis()[0])
    equation.insert(index + 1, get_minus())
    count = 0
    index += 2
    while index < len(equation):
        if equation[index] in get_opening_parenthesis():
            count += 1
        if equation[index] in get_closing_parenthesis():
            count -= 1
        if count == 0:
            if index+ 1 < len(equation):
                if equation[index+1] in get_one_operands_operators_right_side():
                    temp = equation[index+1]
                    equation[index+1] = get_closing_parenthesis()[0]
                    equation.insert(index + 2,temp)
                else:
                    equation.insert(index + 1, get_closing_parenthesis()[0])
            else:
                equation.insert(index + 1, get_closing_parenthesis()[0])
            return equation
        index += 1
    return equation
