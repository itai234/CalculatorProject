from math import pow
from ArithmeticFunctionsEvaluations.Operator import Operator
from ArithmeticFunctionsEvaluations.OperatorFactory import *


class NumbersPower(Operator):
    def execute(self, num1, num2)->float:
        """
        :param num1: first number
        :param num2: second number
        :return: first number power by the second number
        """
        if num1 < 0 and (num2 < 1 and num2 > -1):
            raise ArithmeticError("Cannot Perform sqrt on a negative value")
        if num1 == 0 and num2 <= 0:
            raise ArithmeticError("0 raised to a non-positive power is undefined.")
        try:
            result = pow(num1, num2)
            if result > 10 ** 10000:
                raise OverflowError("Result too large to compute.")
            if result < -(10 ** 10):
                return 0
            return result
        except OverflowError:
            raise Exception("Result too large to compute.")

    def get_side(self) -> str:
        return "Middle"

    def get_priority(self) -> int:
        return OperatorFactory().get_priority("^")
