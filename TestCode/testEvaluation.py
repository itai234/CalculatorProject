
import  pytest
from Evaluation.EvaluatePostFixExpression import EvaluationOfPostFix
from ReformattingEquation.Reformater import Reformat
from Evaluation.TransformInfixToPostFix import *

InfixConverter = InfixToPostfix()


def evaluate_infix(expression):
    """
    A helper function to evaluate an infix expression by using the provided methods.
    """
    try:
        infix_expression = list(Reformat(expression))
        InfixConverter.setExpression(infix_expression)
        InfixConverter.convert()
        postfix_expression = InfixConverter.getPostFix()
        evaluator = EvaluationOfPostFix()
        evaluator.setExpression(postfix_expression)
        result = evaluator.evaluate()
        return result
    except Exception as e:
        return str(e)



# Simple Valid Expressions
def test_simple_addition():
    assert evaluate_infix("2 + 3") == 5

def test_simple_subtraction():
    assert evaluate_infix("8 - 2") == 6

def test_simple_modulo():
    assert evaluate_infix("10 % 3") == 1

def test_simple_minimum():
    assert evaluate_infix("7 $ 5") == 7

def test_simple_maximum():
    assert evaluate_infix("4 & 9") == 4

def test_simple_average():
    assert evaluate_infix("8 @ 2") == 5.0

# Complex Valid Expressions
def test_complex_expression_1():
    assert evaluate_infix("3 + 4 * 2 / 7") == 3 + (4 * 2 / 7)

def test_complex_expression_2():
    assert evaluate_infix("(3 + 5) * (2 - 1)") == (3 + 5) * (2 - 1)

def test_complex_expression_3():
    assert evaluate_infix("3 - 5 + (-4) + 6 / 2") == 3 - 5 + (-4) + 6 / 2

def test_multiple_unary_minus():
    assert evaluate_infix("- - - 3") == -(-(-3))

def test_multiple_unary_minus_with_parentheses():
    assert evaluate_infix("(- - 3) + 2") == -(-3) + 2

# Edge Cases
def test_division_by_zero():
    assert evaluate_infix("10 / 0") == "division by zero"

def test_invalid_syntax_1():
    assert evaluate_infix("2 * ^ 3") == "Invalid expression"

def test_invalid_syntax_2():
    assert evaluate_infix("gibberish") == "Invalid expression"

def test_empty_input():
    assert evaluate_infix("") == "Invalid expression"

def test_whitespace_input():
    assert evaluate_infix("   ") == "Invalid expression"

# More Complex Expressions
def test_complex_expression_with_power():
    assert evaluate_infix("(3 + 5) ^ 2") == (3 + 5) ** 2

def test_complex_expression_with_modulo():
    assert evaluate_infix("10 % (3 + 2)") == 10 % (3 + 2)

def test_complex_expression_long_1():
    assert evaluate_infix("10 + 5 ^ 2 * (8 - 1) / 4 + 6 % 3") == 10 + 5**2 * (8 - 1) / 4 + 6 % 3

def test_complex_expression_long_2():
    assert evaluate_infix("(3 * 2 + 5) / (7 - 4 ^ 2)") == (3 * 2 + 5) / (7 - 4 ** 2)

# Sum of Digits
def test_sum_digits():
    assert evaluate_infix("123 #") == 1 + 2 + 3


# Invalid Syntax Tests
def test_invalid_syntax_missing_operator():
    assert evaluate_infix("2 * ^ 3") == "Invalid expression"

def test_invalid_syntax_missing_operand():
    assert evaluate_infix("5 +") == "Invalid expression"

def test_invalid_syntax_multiple_operators():
    assert evaluate_infix("3 + + 2") == "Invalid expression"

def test_invalid_gibberish():
    assert evaluate_infix("gibberish") == "Invalid expression"

def test_invalid_empty_string():
    assert evaluate_infix("") == "Invalid expression"

def test_invalid_whitespace_string():
    assert evaluate_infix("    ") == "Invalid expression"

# Simple Expressions (One Operator Each)
def test_addition():
    assert evaluate_infix("2 + 3") == 5

def test_subtraction():
    assert evaluate_infix("10 - 6") == 4

def test_multiplication():
    assert evaluate_infix("4 * 5") == 20

def test_division():
    assert evaluate_infix("20 / 4") == 5

def test_exponentiation():
    assert evaluate_infix("2 ^ 3") == 8

def test_modulo():
    assert evaluate_infix("10 % 3") == 1

def test_maximum():
    assert evaluate_infix("8 $ 5") == 8

def test_minimum():
    assert evaluate_infix("3 & 7") == 3

def test_average():
    assert evaluate_infix("6 @ 3") == 4.5

def test_unary_minus():
    assert evaluate_infix("~3") == -3

def test_factorial():
    assert evaluate_infix("5 !") == 120

def test_sum_of_digits():
    assert evaluate_infix("123 #") == 6

# Complex Valid Expressions
def test_complex_expression_1():
    assert evaluate_infix("2 + 3 * 4 - 5") == 2 + 3 * 4 - 5

def test_complex_expression_2():
    assert evaluate_infix("(3 + 4) * (5 - 2)") == (3 + 4) * (5 - 2)

def test_complex_expression_3():
    assert evaluate_infix("10 + (6 / 2) ^ 2 - 5") == 10 + (6 / 2) ** 2 - 5

def test_complex_expression_with_negation():
    assert evaluate_infix("~(3 + 5)") == -(3 + 5)

def test_complex_expression_with_factorial():
    assert evaluate_infix("(3 + 2) !") == "Invalid"

def test_complex_expression_long_1():
    assert evaluate_infix("10 + 2 * (3 ^ 2 - 1) / 4 + 5 % 3") == 10 + 2 * (3 ** 2 - 1) / 4 + 5 % 3

def test_complex_expression_long_2():
    assert evaluate_infix("5 $ (3 + 2 * (6 & 4))") == max(5, (3 + 2 * min(6, 4)))

def test_complex_expression_long_3():
    assert evaluate_infix("(5 * 2 - 3) + (8 / 4 ^ 2)") == (5 * 2 - 3) + (8 / 4 ** 2)

# Edge Cases
def test_multiple_unary_minus():
    assert evaluate_infix("- - - 3") == -(-(-3))

def test_multiple_unary_minus_with_parentheses():
    assert evaluate_infix("(- - 3) + 2") == -(-3) + 2

def test_factorial_with_large_number():
    assert evaluate_infix("10 !") == 3628800

def test_sum_digits_large_number():
    assert evaluate_infix("987654321 #") == 45

def test_average_with_negative_numbers():
    assert evaluate_infix("(-4) @ (-6)") == (-4 + (-6)) / 2

def test_modulo_with_negative_numbers():
    assert evaluate_infix("-10 % 3") == -(10 % 3)

def test_factorial_with_zero():
    assert evaluate_infix("0 !") == 1

def test_zero_division():
    assert evaluate_infix("10 / 0") == "division by zero"

def test_nested_parentheses():
    assert evaluate_infix("((3 + 5) * 2) ^ (1 + 1)") == ((3 + 5) * 2) ** (1 + 1)

# Additional Long Expressions
def test_very_long_expression_1():
    assert evaluate_infix("3 + 5 * (2 ^ 3 - (8 / 4)) - 6 & (10 $ 7)") == \
        3 + 5 * (2 ** 3 - (8 / 4)) - min(6, max(10, 7))

def test_very_long_expression_2():
    assert evaluate_infix("5 + (2 @ (8 & 6)) ^ 2 - 7 $ 3 + 4 * 2") == 22
