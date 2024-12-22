
import pytest
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


def test_simple_valid_expressions():
    assert evaluate_infix("2 + 3") == 5
    assert evaluate_infix("8 - 2") == 6
    assert evaluate_infix("8 * 2") == 16
    assert evaluate_infix("8 / 2") == 4
    assert evaluate_infix("10 % 3") == 1
    assert evaluate_infix("6 ^ 3") == 216
    assert evaluate_infix("7 $ 5") == 7
    assert evaluate_infix("4 & 9") == 4
    assert evaluate_infix("8 @ 2") == 5.0
    assert evaluate_infix("~4") == -4
    assert evaluate_infix("4!") == 24
    assert evaluate_infix("123#") == 6


def test_complex_valid_expressions():
    assert evaluate_infix("3 + 4 * 2 / 7") == 4.142857142857142
    assert evaluate_infix("(3 + 5) * (2 - 1)") == 8
    assert evaluate_infix("3 - 5 + (-4) + 6 / 2") == -3
    assert evaluate_infix("(3 + 5) * 2! + 3!^2") == 52
    assert evaluate_infix("(5 + 2) * 3! - (4 ^ 2) + 6 @ 7") == 32.5
    assert evaluate_infix("- - - 3") == -3
    assert evaluate_infix("(- - 3) + 2") == 5
    assert evaluate_infix("3 + 5 * 2 ^ 3 - 6 / 2") == 40
    assert evaluate_infix("(5 + 2) * 3! - (4 ^ 2) + 6 @ 7") == 32.5
    assert evaluate_infix("3! - 4! * 2!") == -42
    assert evaluate_infix("-3 + -5 ^ 2") == 22
    assert evaluate_infix("5! ^ (3 * 2)") == 120 ** 6
    assert evaluate_infix("(3! + 5) * 2!") == 22
    assert evaluate_infix("(7 % (5 + 2)) + 5") == 5
    assert evaluate_infix("3 + 5 * (3 ^ 2) / (4 - 3) ^ 2") == 48
    assert evaluate_infix("(2 ^ (2 ^ (2 ^ 2)))") == 65536
    assert evaluate_infix("(10 ^ 10) / (5 + 5) * (2 ^ 3)") == 8000000000
    assert evaluate_infix("3 + 5 * 2 ^ 3 - 6 / 2") == 40
    assert evaluate_infix("(3 + 5) * 2! + 3!^2") == 52
    assert evaluate_infix("(5 + 2) * 3! - (4 ^ 2) + 6 @ 7") == 32.5
    assert evaluate_infix("3! - 4! * 2!") == -42.0
    assert evaluate_infix("-3 + -5 ^ 2") == 22
    assert evaluate_infix("342 + 512 * (33 ^ 2) / (41 - 35) ^ 2+123") == 15953
    assert evaluate_infix("1234567# + (9999 * 3)") == 30025
    assert evaluate_infix("(456# * 10) + 9999 ^ 2") == 99980151
    assert evaluate_infix("(50$40) * (20%3) + 100!") == 9.332621544394415e+157
    assert evaluate_infix("(3000 & 5000) ^ (3!)") == 7.29e+20
    assert evaluate_infix("(987# * 100) - (2!)") == 2398
    assert evaluate_infix("(10 ^ 10) / 3! - 25#") == 1666666659.6666667
    assert evaluate_infix("(9876$5432) / (9 * 8)") == 137.16666666666666
    assert evaluate_infix("(7! + 15@5) ^ 2") == 25502500
    assert evaluate_infix("((12345#) * 10) + 4!") == 174
    assert evaluate_infix("((50 * 3) ^ 2) - 12!") == -478979100
    assert evaluate_infix("((1234567# + 50!) - 99999) / 3!") == 5.069015533618896e+63
    assert evaluate_infix("((2000$5000) ^ (9 - 4!)) + (123# * 7)") == 42
    assert evaluate_infix("(987654321# + (10 ^ 5)) * 50") == 5002250
    assert evaluate_infix("(6! + 500) / ((15@5) ^ 2)") == 12.2
    assert evaluate_infix("(4000 & 9000) * ((10 ^ 2) + 123#)") == 424000
    assert evaluate_infix("((987$6543) / 3!) ^ (456#)") == 3.667626049953535e+45
    assert evaluate_infix("((9876@5432) + (9!)) - (7! * 2)") == 360454
    assert evaluate_infix("((1234 + 5678) % 200) * (100!)") == 1.0452536129721744e+160
    assert evaluate_infix("(10! * (123456789#)) - (50 / 5)") == 163295990
    assert evaluate_infix("((12345@67890) + (7!)) * ((10$5) + 123#)") == 722520


def test_invalid_syntax():
    print(evaluate_infix("2 * ^ 3"))
    print(evaluate_infix("5 +"))
    print(evaluate_infix("gibberish"))
    print(evaluate_infix("2 * ^ 3"))
    print(evaluate_infix("2 @ 3 ?"))
    print(evaluate_infix("(3 + 5"))
    print(evaluate_infix("3 + (2 * 3"))
    print(evaluate_infix("3 + 5)"))
    print(evaluate_infix("~ + 2"))
    print(evaluate_infix("10 %% 3"))
    print(evaluate_infix("5 $ @ 3"))
    print(evaluate_infix("3 @ + 4"))
    print(evaluate_infix(""))
    print(evaluate_infix("   "))
    print(evaluate_infix("3 + (2 - 1"))
    print(evaluate_infix("3 & @ 2"))
    print(evaluate_infix("! 5"))
    print(evaluate_infix("5 ! +") )
    print(evaluate_infix("5a + 3"))
    print(evaluate_infix("2 ^^ 3"))
    print(evaluate_infix("(3 + )"))
    print(evaluate_infix("()") )
    print(evaluate_infix("123 $"))
    print(evaluate_infix("10 / 0"))
    print(evaluate_infix("10 % 0"))
    print(evaluate_infix("2--3!"))
    print(evaluate_infix("(2---3!)^((~-3!)@5)"))
    print(evaluate_infix("10 ^ 99999 / (3 + 0)"))
    print(evaluate_infix("3 + -3!"))
    print(evaluate_infix("10 ^ 99999 / (3 + 0)"))
    print(evaluate_infix("99999 ^ 1000 / (10 + 5.2)"))


def test_special_cases():

    assert evaluate_infix("~-3!") == 6
    assert evaluate_infix("~(-3)!") == 6
    assert evaluate_infix("3 + 5 * 2 ^ 3 - 4 / 2") == 41
    assert evaluate_infix("3! - ~-10^2 @5*2 + ~4 &9") == -6322.555320336759
    assert evaluate_infix("~(9!)@3") == -181438.5
    assert evaluate_infix("~-3!") == 6
    assert evaluate_infix("-(~(10))") == 10
    assert evaluate_infix("-~10") == 10
    assert evaluate_infix("~-3!") == 6
    assert evaluate_infix("(3 + 5) ^ 2") == (3 + 5) ** 2
    assert evaluate_infix("10 % (3 + 2)") == 10 % (3 + 2)
    assert evaluate_infix("10 + 5 ^ 2 * (8 - 1) / 4 + 6 % 3") == 10 + 5 ** 2 * (8 - 1) / 4 + 6 % 3
    assert evaluate_infix("(3 * 2 + 5) / (7 - 4 ^ 2)") == (3 * 2 + 5) / (7 - 4 ** 2)
    assert evaluate_infix("2 $ 3 #") == 3
    assert evaluate_infix("123 # * 2") == 12


