from ArithmeticFunctionsEvaluations.Operator import Operator
from ArithmeticFunctionsEvaluations.Properties import *


class NumberNeg(Operator):
    def execute(self, num1, num2=None):
        """
        :param num1: operand
        :return: return the opposite sign number
        """
        return -num1

    def get_side(self) -> str:
        return "left"

    def get_priority(self) -> int:
        return get_priority("~")
