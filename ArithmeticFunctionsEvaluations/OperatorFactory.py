
from ArithmeticFunctionsEvaluations.CalculatorProperties import *

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
        if not hasattr(self, "_initialized"):
            self._operators = OPERATORS
            self._Priorities = PRIORITIES
            self._two_operands_operators = []
            self._one_operands_operators = []
            self._one_operands_operators_left = []
            self._one_operands_operators_right =  []
            for key in self._operators.keys():
                side = self.get_side(key)
                if side == "Middle":
                    self._two_operands_operators.append(key)
                if side == "left":
                    self._one_operands_operators.append(key)
                    self._one_operands_operators_left.append(key)
                if side == "right":
                    self._one_operands_operators.append(key)
                    self._one_operands_operators_right.append(key)
            self._numbers = NUMBERS
            self._parenthesis = PARENTHESIS
            self._floating_point = FLOATING_POINT
            self._initialized = True
    def operation(self, operator_type, num1, num2=None) -> float:
        """
        this function performs the calculation , it receives the operator type like +, - and more ,
        it gets two numbers but if receives one number then the other is None by default (if the user wants Factorial
        or Neg) and it calls the relevant function .
        """
        return self._operators.get(operator_type)().execute(num1, num2)

    def get_operators(self) -> list:
        return list(self._operators.keys())

    def get_numbers(self) -> list:
        return list(self._numbers)

    def get_parenthesis(self) -> list:
        return list(self._parenthesis)

    def get_floating_point(self) -> list:
        return list(self._floating_point)

    def get_opening_parenthesis(self) -> list:
        return list(self._parenthesis[0])

    def get_closing_parenthesis(self) -> list:
        return list(self._parenthesis[1])

    def get_two_operands_operators(self) -> list:
        return list(self._two_operands_operators)

    def get_one_operands_operators(self) -> list:
        return list(self._one_operands_operators)

    def get_one_operands_operators_left_side(self) -> list:
        return list(self._one_operands_operators_left)

    def get_one_operands_operators_right_side(self) -> list:
        return list(self._one_operands_operators_right)

    def get_priority(self, operator: str) -> int:
        return self._Priorities.get(operator)

    def get_side(self, operator: str) -> str:
        operator_class = self._operators.get(operator)
        if operator_class is None:
            raise ValueError(f"Operator '{operator}' is not defined.")
        return operator_class().get_side()

    def get_parenthesis_pairs(self) -> dict:
        return {self._parenthesis[0]: self._parenthesis[1]}

    def get_all_legal_letters(self) -> list:
        return list(self.get_operators() + self.get_numbers() + self.get_parenthesis() + self.get_floating_point())

    def get_minus(self) -> str:
        return "-"
