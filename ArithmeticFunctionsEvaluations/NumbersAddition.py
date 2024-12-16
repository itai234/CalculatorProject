from ArithmeticFunctionsEvaluations.Operator import Operator
from ArithmeticFunctionsEvaluations.OperatorFactory import *


class NumbersAddition(Operator):
    def execute(self, num1, num2):
        """
        the function returns the sum of the two numbers given to it
        """
        return num1 + num2

    def get_side(self) -> str:
        return "Middle"

    def get_priority(self) -> int:
        return OperatorFactory().get_priority("+")
