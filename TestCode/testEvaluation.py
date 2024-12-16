
import  pytest
from Evaluation.EvaluatePostFixExpression import EvaluationOfPostFix
from ReformattingEquation.Reformater import reformat
from Evaluation.TransformInfixToPostFix import *

InfixConverter = InfixToPostfix()


def evaluate_infix(expression):
    """
    A helper function to evaluate an infix expression by using the provided methods.
    """
    try:
        infix_expression = list(reformat(expression))
        InfixConverter.set_expression(infix_expression)
        InfixConverter.convert()
        postfix_expression = InfixConverter.get_post_fix()
        evaluator = EvaluationOfPostFix()
        evaluator.set_expression(postfix_expression)
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

def test_complex_expression_with_negation():
    assert evaluate_infix("~(3 + 5)") == -(3 + 5)

def test_complex_expression_with_factorial():
    assert evaluate_infix("(3 + 2) !") == "Invalid"

def test_complex_expression_long_3():
    assert evaluate_infix("(5 * 2 - 3) + (8 / 4 ^ 2)") == (5 * 2 - 3) + (8 / 4 ** 2)

# Edge Cases


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

def test_zero_division2():
    assert evaluate_infix("10 / 0") == "division by zero"

def test_nested_parentheses2():
    assert evaluate_infix("((3 + 5) * 2) ^ (1 + 1)") == ((3 + 5) * 2) ** (1 + 1)


# Missing operands or operators
def test_missing_operator():
    assert evaluate_infix("2 +") == "Invalid expression"

def test_missing_operand():
    assert evaluate_infix("+ 2") == "Invalid expression"

def test_multiple_operators():
    assert evaluate_infix("2 + + 3") == "Invalid expression"

# Invalid syntax
def test_invalid_operator():
    assert evaluate_infix("2 * ^ 3") == "Invalid expression"

def test_invalid_character():
    assert evaluate_infix("2 $ 3 #") == "Invalid expression"

def test_unexpected_character():
    assert evaluate_infix("2 @ 3 ?") == "Invalid expression"

# Parenthesis issues
def test_unmatched_parenthesis():
    assert evaluate_infix("(3 + 5") == "Unmatched parenthesis"

def test_missing_closing_parenthesis():
    assert evaluate_infix("3 + (2 * 3") == "Unmatched parenthesis"

def test_unexpected_closing_parenthesis():
    assert evaluate_infix("3 + 5)") == "Unmatched parenthesis"

# Improper unary minus usage
def test_unary_minus_with_operator():
    assert evaluate_infix("~ + 2") == "Invalid expression"

def test_double_unary_minus():
    assert evaluate_infix("~- 2") == "Invalid expression"

# Invalid use of special operators
def test_invalid_modulo_syntax():
    assert evaluate_infix("10 %% 3") == "Invalid expression"

def test_invalid_max_operator():
    assert evaluate_infix("5 $ @ 3") == "Invalid expression"

def test_invalid_average_operator():
    assert evaluate_infix("3 @ + 4") == "Invalid expression"

# Empty input
def test_empty_input1():
    assert evaluate_infix("") == "Invalid expression"

# Whitespace only input
def test_whitespace_input1():
    assert evaluate_infix("   ") == "Invalid expression"


# Malformed expressions
def test_malformed_expression():
    assert evaluate_infix("3 + (2 - 1") == "Unmatched parenthesis"

def test_unexpected_symbol():
    assert evaluate_infix("3 & @ 2") == "Invalid expression"

# Invalid usage of factorial
def test_factorial_without_number():
    assert evaluate_infix("! 5") == "Invalid expression"

def test_factorial_with_invalid_operand():
    assert evaluate_infix("5 ! +") == "Invalid expression"

# Invalid characters in the equation
def test_invalid_character_in_number():
    assert evaluate_infix("5a + 3") == "Invalid expression"


# Extra operators


# Invalid exponentiation
def test_invalid_exponentiation_operator():
    assert evaluate_infix("2 ^^ 3") == "Invalid expression"

# Complex invalid expressions
def test_missing_operand_in_parentheses():
    assert evaluate_infix("(3 + )") == "Invalid expression"

def test_empty_parentheses():
    assert evaluate_infix("()") == "Invalid expression"

# Invalid sum of digits
def test_invalid_sum_digits():
    assert evaluate_infix("123 $") == "Invalid expression"

# Division by zero
def test_division_by_zero():
    assert evaluate_infix("10 / 0") == "division by zero"

def test_modulo_by_zero():
    assert evaluate_infix("10 % 0") == "division by zero"

# Invalid sum of digits expression
def test_invalid_sum_digits_expression():
    assert evaluate_infix("123 # * 2") == "Invalid expression"

def test_final1():
    assert evaluate_infix("2--3!") == "Invalid expression"
def test_final2():
    assert evaluate_infix("~-3!") == 6

def test_final3():
    assert evaluate_infix("~(-3)!") == 6

def test_final4():
    print(evaluate_infix("3~3"))

def test_final5():
    print( evaluate_infix("3~"))



def test_complex_power():
       print( evaluate_infix("(2---3!)^((~--3!)@5)"))

def test_complex_precedence_no_parentheses():
    assert evaluate_infix("3+5*2^2-4/2") == 21

def test_complex_precedence_mix():
    assert evaluate_infix("3! - ~-10^2 @5*2 + ~4 &9") == -6322.555320336759

def test_tilde_on_factorial_with_average():
    assert evaluate_infix("~(9!)@3") == -181438.5

def test_tilde_multiple_unary_minus_factorial():
        print(evaluate_infix("~--3!"))

def test_nested_tilde_with_parentheses():
    assert evaluate_infix("-(~(10))") == 10

def test_signs_with_tilde():
    assert evaluate_infix("-~10") == 10

def test_expr_tilde_minus_3_factorial():
    assert evaluate_infix("~-3!") == 6

def test_expr_minus_minus_tilde_minus_minus_3():
        print(evaluate_infix("--~--3"))

def test_expr_2_minus_minus_3_factorial():
       print(evaluate_infix("2 - - 3!"))