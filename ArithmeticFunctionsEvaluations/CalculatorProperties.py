from ArithmeticFunctionsEvaluations.NumberUnaryMinus import NumberUnaryMinus
from ArithmeticFunctionsEvaluations.NumbersAvg import NumbersAvg
from ArithmeticFunctionsEvaluations.NumbersDivision import NumbersDivision
from ArithmeticFunctionsEvaluations.NumberNeg import NumberNeg
from ArithmeticFunctionsEvaluations.NumbersAddition import NumbersAddition
from ArithmeticFunctionsEvaluations.NumbersSubtraction import NumbersSubtraction
from ArithmeticFunctionsEvaluations.NumbersMultiplication import NumbersMultiplication
from ArithmeticFunctionsEvaluations.NumbersModulo import NumbersModulo
from ArithmeticFunctionsEvaluations.NumbersPower import NumbersPower
from ArithmeticFunctionsEvaluations.NumbersMinimum import NumbersMinimum
from ArithmeticFunctionsEvaluations.NumbersMaximum import NumbersMaximum
from ArithmeticFunctionsEvaluations.NumberFactorial import NumberFactorial
from ArithmeticFunctionsEvaluations.NumberSumDigits import NumberSumDigits

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
NUMBERS = list("0123456789")
PARENTHESIS = list("()")
FLOATING_POINT = ['.']
