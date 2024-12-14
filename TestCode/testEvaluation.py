
import  pytest
from Evaluation.EvaluatePostFixExpression import *
evaluator = EvaluationOfPostFix()


def test_addition():
    expression = [ '3', '!']  # 2 + 3
    evaluator.setExpression(expression)
    print(evaluator.evaluate())  # Expected: 5

def test_subtraction():
    expression = ['10', '5', '-']  # 10 - 5
    evaluator.setExpression(expression)
    print(evaluator.evaluate())  # Expected: 5

def test_multiplication():
    expression = ['4', '5', '*']  # 4 * 5
    evaluator.setExpression(expression)
    print(evaluator.evaluate())  # Expected: 20

def test_division():
    expression = ['20', '4', '/']  # 20 / 4
    evaluator.setExpression(expression)
    print(evaluator.evaluate())  # Expected: 5

def test_mixed_operations_1():
    expression = ['2', '3', '1', '*', '+', '9', '-']  # 2 + (3 * 1) - 9
    evaluator.setExpression(expression)
    print(evaluator.evaluate())  # Expected: -4

def test_mixed_operations_2():
    expression = ['5', '1', '2', '+', '4', '*', '+', '3', '-']  # 5 + ((1 + 2) * 4) - 3
    evaluator.setExpression(expression)
    print(evaluator.evaluate())  # Expected: 14

def test_unary_minus_1():
    expression = ['3', 'Unary', '5', '+']  # -3 + 5
    evaluator.setExpression(expression)
    print(evaluator.evaluate())  # Expected: 2

def test_unary_minus_2():
    expression = ['5', '2', '^', 'Unary']  # - (5^2)
    evaluator.setExpression(expression)
    print(evaluator.evaluate())  # Expected: -25

def test_exponentiation():
    expression = ['2', '3', '^']  # 2^3
    evaluator.setExpression(expression)
    print(evaluator.evaluate())  # Expected: 8

def test_exponentiation_with_unary():
    expression = ['2', '3', '^', 'Unary']  # - (2^3)
    evaluator.setExpression(expression)
    print(evaluator.evaluate())  # Expected: -8

def test_single_operand():
    expression = ['42']  # Just a single number
    evaluator.setExpression(expression)
    print(evaluator.evaluate())  # Expected: 42


def test_division_by_zero():
    expression = ['10', '0', '/']  # 10 / 0
    try:
        evaluator.setExpression(expression)
        print(evaluator.evaluate())
    except ZeroDivisionError as e:
        print(e)  # Expected: ZeroDivisionError


def test_invalid_expression():
    expression = ['2', '+']  # Missing operand
    try:
        evaluator.setExpression(expression)
        print(evaluator.evaluate())
    except ValueError as e:
        print(e)  # Expected: ValueError (Invalid postfix expression)


def test_complex_expression_1():
    expression = ['3', '4', '+', '2', '*', '7', '/']  # ((3 + 4) * 2) / 7
    evaluator.setExpression(expression)
    print(evaluator.evaluate())  # Expected: 2.0

def test_complex_expression_2():
    expression = ['5', '1', '2', '+', '4', '*', '+', '3', '-', '2', '^']  # (5 + ((1 + 2) * 4) - 3)^2
    evaluator.setExpression(expression)
    print(evaluator.evaluate())  # Expected: 196
