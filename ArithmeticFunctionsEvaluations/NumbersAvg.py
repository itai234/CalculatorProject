from ArithmeticFunctionsEvaluations.Operator import Operator
from ArithmeticFunctionsEvaluations.OperatorFactory import *


class NumbersAvg(Operator):
    def execute(self, num1, num2):
        """
        :param num1: operand1
        :param num2: operand2
        :return: return the average of the operands
        """
        return (num1 + num2) / 2

    def get_side(self) -> str:
        return "Middle"

    def get_priority(self) -> int:
        return OperatorFactory().get_priority("@")