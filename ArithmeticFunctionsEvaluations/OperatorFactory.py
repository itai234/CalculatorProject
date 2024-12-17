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


class OperatorFactory:
    """
    this factory will have all the operators classes evaluations performed by him
    it will have his dict of operators that each has the value of the class of the operator and will perform
    the calculations.
    the factory is a singleton
    """
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(OperatorFactory, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        # has a operators dict with references to their classes
        # and a dict of the operators with their properties
        self._operators = {
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
        self._Priorities = {
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

    def operation(self, operator_type, num1, num2=None) -> float:
        """
        this function performs the calculation , it receives the operator type like +, - and more ,
        it gets two numbers but if receives one number then the other is None by defult (if the user wants Factorial
        or Neg) and it calls the relevant function .
        """
        operator_class = self._operators.get(operator_type)
        if operator_class is None:
            raise ValueError(f"No Such Operator as : {operator_type}")
        operator_instance = operator_class()
        return operator_instance.execute(num1, num2)

    def get_operators(self) -> list:
        return list(self._operators.keys())

    def get_numbers(self) -> list:
        return list("0123456789")

    def get_parenthesis(self) -> list:
        return list("()")

    def get_floating_point(self) -> list:
        return list(".")

    def get_opening_parenthesis(self) -> list:
        return list("(")

    def get_closing_parenthesis(self) -> list:
        return list(")")

    def get_two_operands_operators(self) -> list:
        return list("+-*/^%$&@")

    def get_one_operands_operators(self) -> list:
        return list("#~!")

    def get_one_operands_operators_left_side(self) -> list:
        return list("~")

    def get_one_operands_operators_right_side(self) -> list:
        return list("#!")

    def get_priority(self, operator: str) -> int:
        return self._Priorities.get(operator)

    def get_side(self, operator: str) -> str:
        operator_class = self._operators.get(operator)
        if operator_class is None:
            raise ValueError(f"Operator '{operator}' is not defined.")
        return operator_class().get_side()

    def get_parenthesis_pairs(self) -> dict:
        return {'(': ')'}

    def get_all_legal_letters(self) -> list:
        return list(self.get_operators() + self.get_numbers() + self.get_parenthesis() + self.get_floating_point())

    def get_minus(self) -> str:
        return "-"
