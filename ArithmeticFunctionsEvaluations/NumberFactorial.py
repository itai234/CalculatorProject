from ArithmeticFunctionsEvaluations.Operator import Operator
from ArithmeticFunctionsEvaluations.OperatorFactory import *
class NumberFactorial(Operator):
    def execute(self, num1 , num2 = None):
        """
        :param num: operand
        :return: the factorial of the number given
        """
        if num1 < 0 or not type(num1) == int:
            raise ValueError("Factorial is only for the positive integers")
        result = 1
        for i in range(1, num1+ 1):
            result *= i
        return result


    def getSide(self) -> str:
        return "right"

    def getPriority(self) -> int:
        return OperatorFactory().getPriority("!")

