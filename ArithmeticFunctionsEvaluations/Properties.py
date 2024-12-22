from ArithmeticFunctionsEvaluations.NumberFactorial import NumberFactorial
from ArithmeticFunctionsEvaluations.NumberNeg import NumberNeg
from ArithmeticFunctionsEvaluations.NumberSumDigits import NumberSumDigits
from ArithmeticFunctionsEvaluations.NumberUnaryMinus import NumberUnaryMinus
from ArithmeticFunctionsEvaluations.NumbersAddition import NumbersAddition
from ArithmeticFunctionsEvaluations.NumbersAvg import NumbersAvg
from ArithmeticFunctionsEvaluations.NumbersDivision import NumbersDivision
from ArithmeticFunctionsEvaluations.NumbersMaximum import NumbersMaximum
from ArithmeticFunctionsEvaluations.NumbersMinimum import NumbersMinimum
from ArithmeticFunctionsEvaluations.NumbersModulo import NumbersModulo
from ArithmeticFunctionsEvaluations.NumbersMultiplication import NumbersMultiplication
from ArithmeticFunctionsEvaluations.NumbersPower import NumbersPower
from ArithmeticFunctionsEvaluations.NumbersSubtraction import NumbersSubtraction

OPERATORS = {
    '+': NumbersAddition,
    '-': NumbersSubtraction,
    '*': NumbersMultiplication,
    '/': NumbersDivision,
    '^': NumbersPower,
    '%': NumbersModulo,
    '$': NumbersMaximum,
    '&': NumbersMinimum,
    '@': NumbersAvg,
    '~': NumberNeg,
    '!': NumberFactorial,
    '#': NumberSumDigits,
    'Unary': NumberUnaryMinus
}

PRIORITIES = {

    '+': 1,
    '-': 1,
    '*': 2,
    '/': 2,
    '^': 3,
    '%': 4,
    '$': 5,
    '&': 5,
    '@': 5,
    '~': 6,
    '!': 6,
    '#': 6,
    'Unary': 2.5
}


def get_side(operator: str) -> str:
    operator_class = OPERATORS.get(operator)
    if operator_class is None:
        raise ValueError(f"Operator '{operator}' is not defined.")
    return operator_class().get_side()


NUMBERS = list("0123456789")
PARENTHESIS = list("()")
FLOATING_POINT = ['.']
TWO_OPERANDS_OPERATORS = []
ONE_OPERAND_OPERATORS = []
ONE_OPERAND_OPERATORS_LEFT = []
ONE_OPERAND_OPERATORS_RIGHT = []
MINUS = "-"
for key in OPERATORS.keys():
    side = get_side(key)
    if side == "Middle":
        TWO_OPERANDS_OPERATORS.append(key)
    if side == "left":
        ONE_OPERAND_OPERATORS.append(key)
        ONE_OPERAND_OPERATORS_LEFT.append(key)
    if side == "right":
        ONE_OPERAND_OPERATORS.append(key)
        ONE_OPERAND_OPERATORS_RIGHT.append(key)


def get_all_legal_letters() -> list:
    return list(list(OPERATORS.keys()) + NUMBERS + PARENTHESIS + FLOATING_POINT)


def get_priority(operator: str) -> int:
    return PRIORITIES.get(operator)


def get_operators() -> list:
    return list(OPERATORS.keys())
