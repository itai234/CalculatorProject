from multiprocessing.managers import Value

from ArithmeticFunctionsEvaluations.Operator import Operator
from ArithmeticFunctionsEvaluations.OperatorFactory import *
class NumberFactorial(Operator):
    def execute(self, num1 , num2 = None):
        """
        :param num: operand
        :return: the factorial of the number given
        """
        if num1 < 0 or not type(num1) == float:
            raise ValueError("Factorial is only for the positive integers")
        if isinstance(num1, float):
            if num1.is_integer():
                num1 = int(num1)
            else:
                raise ValueError("Cannot perform Factorial on non-integer float numbers")
        elif not isinstance(num1, int):
            raise ValueError("Factorial is only for integers")

        result = 1
        iterationLimit = 10 ** 6
        iterationCounter = 0
        for i in range(1 , num1 + 1):
            result *= i
            iterationCounter += 1
            if iterationCounter > iterationLimit:
                raise Exception("Cannot perform factorial on very large numbers. Computation taking too long.")
            if result > 10 ** 10000:
                raise Exception("Result too large to compute factorial for this number.")
        return result

    def getSide(self) -> str:
        return "right"

    def getPriority(self) -> int:
        return OperatorFactory().getPriority("!")

