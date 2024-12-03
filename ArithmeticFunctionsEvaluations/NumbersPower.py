from math import pow
from ArithmeticFunctionsEvaluations.Operator import Operator

class NumbersPower(Operator):
    def execute(self, num1, num2):
        """
        :param num1: first number
        :param num2: second number
        :return: first number power by the second number
        """
        return pow(num1, num2)
