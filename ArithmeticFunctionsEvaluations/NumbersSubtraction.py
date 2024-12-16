from ArithmeticFunctionsEvaluations.Operator import Operator
from ArithmeticFunctionsEvaluations.OperatorFactory import *


class NumbersSubtraction(Operator):
    def execute(self, num1, num2):
        """
        the function returns the sub of the second number from the first
        """
        return num1 - num2

    def get_side(self) -> str:
        return "Middle"

    def get_priority(self) -> int:
        return OperatorFactory().get_priority("-")


