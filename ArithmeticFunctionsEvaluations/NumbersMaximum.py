from ArithmeticFunctionsEvaluations.Operator import Operator
from ArithmeticFunctionsEvaluations.Properties import *


class NumbersMaximum(Operator):
    def execute(self, num1, num2):
        """
        :param num1: operand1
        :param num2: operand2
        :return: return the maximum of the operands
        """
        if num1 > num2:
            return num1
        return num2

    def get_side(self) -> str:
        return "Middle"

    def get_priority(self) -> int:
        return get_priority("$")
