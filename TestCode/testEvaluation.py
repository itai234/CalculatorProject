
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
    assert evaluate_infix("123#") ==6

def test_complex_valid_expressions():
    assert evaluate_infix("3 + 4 * 2 / 7") == 3 + (4 * 2 / 7)
    assert evaluate_infix("(3 + 5) * (2 - 1)") == (3 + 5) * (2 - 1)
    assert evaluate_infix("3 - 5 + (-4) + 6 / 2") == 3 - 5 + (-4) + 6 / 2
    assert evaluate_infix("(3 + 5) * 2! + 3!^2") == (3 + 5) * 2 + 6**2
    assert evaluate_infix("(5 + 2) * 3! - (4 ^ 2) + 6 @ 7") == (5 + 2) * 6 - (4 ** 2) + 6.5
    assert evaluate_infix("- - - 3") == -(-(-3))
    assert evaluate_infix("(- - 3) + 2") == -(-3) + 2


# Function to test edge cases
def test_edge_cases():
    print( evaluate_infix("10 / 0") )
    print( evaluate_infix("2 * ^ 3") )
    print( evaluate_infix("gibberish"))
    print( evaluate_infix("") )
    print( evaluate_infix("   ") )
    assert evaluate_infix("(3 + 5) ^ 2") == (3 + 5) ** 2
    assert evaluate_infix("10 % (3 + 2)") == 10 % (3 + 2)
    assert evaluate_infix("10 + 5 ^ 2 * (8 - 1) / 4 + 6 % 3") == 10 + 5**2 * (8 - 1) / 4 + 6 % 3
    assert evaluate_infix("(3 * 2 + 5) / (7 - 4 ^ 2)") == (3 * 2 + 5) / (7 - 4 ** 2)
    assert evaluate_infix("2 $ 3 #") == 3
    assert evaluate_infix("123 # * 2") == 12

# Function to test invalid syntax errors
def test_invalid_syntax():
    print( evaluate_infix("2 * ^ 3") )
    print( evaluate_infix("5 +") )
    print( evaluate_infix("gibberish") )
    print( evaluate_infix("2 * ^ 3") )
    print( evaluate_infix("2 @ 3 ?") )
    print( evaluate_infix("(3 + 5") )
    print( evaluate_infix("3 + (2 * 3") )
    print( evaluate_infix("3 + 5)"))
    print( evaluate_infix("~ + 2"))
    print( evaluate_infix("~- 2"))
    print( evaluate_infix("10 %% 3"))
    print( evaluate_infix("5 $ @ 3"))
    print( evaluate_infix("3 @ + 4"))
    print( evaluate_infix(""))
    print( evaluate_infix("   "))
    print( evaluate_infix("3 + (2 - 1"))
    print( evaluate_infix("3 & @ 2"))
    print( evaluate_infix("! 5"))
    print( evaluate_infix("5 ! +") )
    print( evaluate_infix("5a + 3"))
    print( evaluate_infix("2 ^^ 3"))
    print( evaluate_infix("(3 + )"))
    print( evaluate_infix("()") )
    print( evaluate_infix("123 $"))
    print( evaluate_infix("10 / 0"))
    print( evaluate_infix("10 % 0") )
    print( evaluate_infix("2--3!") )
    print( evaluate_infix("(2---3!)^((~-3!)@5)"))
# Function to test complex expressions with factorial, exponentiation, and others
def test_complex_expressions():
    assert evaluate_infix("3 + 5 * 2 ^ 3 - 6 / 2") == 3 + 5 * (2 ** 3) - 6 / 2
    assert evaluate_infix("(3 + 5) * 2! + 3!^2") == (3 + 5) * 2 + 6**2
    assert evaluate_infix("(5 + 2) * 3! - (4 ^ 2) + 6 @ 7") == (5 + 2) * 6 - (4 ** 2) + 6.5
    assert evaluate_infix("3! - 4! * 2!") == 6 - (24 * 2)
    assert evaluate_infix("-3 + -5 ^ 2") == -3 + ((-5) ** 2)
    assert evaluate_infix("5! ^ (3 * 2)") == (120 ** (3 * 2))
    assert evaluate_infix("(3! + 5) * 2!") == (6 + 5) * 2
    assert evaluate_infix("(7 % (5 + 2)) + 5") == (7 % (5 + 2)) + 5
    print(evaluate_infix("10 ^ 99999 / (3 + 0)"))
    assert evaluate_infix("3 + 5 * (3 ^ 2) / (4 - 3) ^ 2") == 3 + 5 * (3 ** 2) / (4 - 3) ** 2
    assert evaluate_infix("(2 ^ (2 ^ (2 ^ 2)))") == (2 ** (2 ** (2 ** 2)))
    assert evaluate_infix("(10 ^ 10) / (5 + 5) * (2 ^ 3)") == (10 ** 10) / (5 + 5) * (2 ** 3)


# Function to test additional edge cases with special expressions
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


def test_complex_expression():
    assert evaluate_infix("3 + 5 * 2 ^ 3 - 6 / 2") == 3 + 5 * (2 ** 3) - 6 / 2
    assert evaluate_infix("(3 + 5) * 2! + 3!^2") == (3 + 5) * 2 + 6**2
    assert evaluate_infix("(5 + 2) * 3! - (4 ^ 2) + 6 @ 7") == (5 + 2) * 6 - (4 ** 2) + 6.5
    assert evaluate_infix("3! - 4! * 2!") == 6 - (24 * 2)
    print( evaluate_infix("3 + -3!") )
    assert evaluate_infix("-3 + -5 ^ 2") == -3 + ((-5) ** 2)
    assert evaluate_infix("5! ^ (3 * 2)") == (120 ** (3 * 2))
    assert evaluate_infix("(3! + 5) * 2!") == (6 + 5) * 2
    assert evaluate_infix("(7 % (5 + 2)) + 5") == (7 % (5 + 2)) + 5
    print( evaluate_infix("10 ^ 99999 / (3 + 0)") )
    assert evaluate_infix("3 + 5 * (3 ^ 2) / (4 - 3) ^ 2") == 3 + 5 * (3 ** 2) / (4 - 3) ** 2
    assert evaluate_infix("(2 ^ (2 ^ (2 ^ 2)))") == (2 ** (2 ** (2 ** 2)))  # Exponential recursion
    assert evaluate_infix("(10 ^ 10) / (5 + 5) * (2 ^ 3)") == (10 ** 10) / (5 + 5) * (2 ** 3)
    assert evaluate_infix("3.5 * 2.7 + (5 ^ 2.5) - 1.2") == 3.5 * 2.7 + (5 ** 2.5) - 1.2
    assert evaluate_infix("9999999999 * 9999999999 / (3 + 0) - 2") == (9999999999 * 9999999999) / 3 - 2
    assert evaluate_infix("(3 + 5) ^ (2 + 5) * 4") == (3 + 5) ** (2 + 5) * 4
    print( evaluate_infix("99999 ^ 1000 / (10 + 5.2)"))
    assert evaluate_infix("3! + 2! ^ 3") == 6 + 2**3
    assert evaluate_infix("3! - 2 * 3") == 6 - 2 * 3
    assert evaluate_infix("(5 + 2) ^ (3 * 2!)") == (5 + 2) ** (3 * 2)
    assert evaluate_infix("3! + (5 * 2) / (3 - 1)") == 6 + (5 * 2) / (3 - 1)
    assert evaluate_infix("5! ^ (3 * 2)") == ((5*4*3*2*1) ** (3 * 2))
    assert evaluate_infix("3 + (7 * 2) / (3 - 2)") == 3 + (7 * 2) / (3 - 2)
    assert evaluate_infix("3 + (5 * 3 / 2) ^ 2 - (4 * 2) / 5") == 3 + (5 * 3 / 2) ** 2 - (4 * 2) / 5
    assert evaluate_infix("(-3 + 5) * 2 @ 4") == (-3 + 5) * 3
    assert evaluate_infix("((2 + 3) * 3!) ^ 2 + (4 + 5) * 6") == ((2 + 3) * 6) ** 2 + (4 + 5) * 6
