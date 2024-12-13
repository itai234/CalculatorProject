from ArithmeticFunctionsEvaluations.Operator import Operator
from ArithmeticFunctionsEvaluations.OperatorFactory import *


class NumberNeg(Operator):
    def execute(self, num1, num2 = None):
        """
        :param num1: operand
        :return: return the opposite sign number
        """
        return -num1


    def getSide(self) -> str:
        return "left"

    def getPriority(self) -> int:
        return OperatorFactory().getPriority("~")
