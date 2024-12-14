from ArithmeticFunctionsEvaluations.Operator import Operator
from ArithmeticFunctionsEvaluations.OperatorFactory import *


class NumberUnaryMinus(Operator):
    def execute(self, num1, num2 = None):
        """
        :param num1: first number
        :param num2:
        :return: negative for the num1
        """
        return -num1
    def getSide(self) -> str:
        return "left"

    def getPriority(self) -> int:
        return OperatorFactory().getPriority("Unary")