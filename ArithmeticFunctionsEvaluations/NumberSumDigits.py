from ArithmeticFunctionsEvaluations.Operator import Operator
from ArithmeticFunctionsEvaluations.OperatorFactory import *


class NumberSumDigits(Operator):
    def execute(self, num1, num2 = None):
        """
        the function returns the sub of the second number from the first
        """
        if num1 < 0:
            raise ValueError("Cannot sum digits of a negative number")
        if isinstance(num1, float):
            num1 = str(num1).replace(".", "")
        num_str = str(num1)
        if not num_str.isdigit():
            raise ValueError("Invalid input for this action")
        while len(num_str) > 1:
            sum_digits = 0
            for x in num_str:
                sum_digits += int(x)
            num_str = str(sum_digits)
        return int(num_str)

    def getSide(self) -> str:
        return "right"

    def getPriority(self) -> int:
        return OperatorFactory().getPriority("#")

