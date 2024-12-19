from ArithmeticFunctionsEvaluations.Operator import Operator
from ArithmeticFunctionsEvaluations.OperatorFactory import *


class NumberSumDigits(Operator):
    def execute(self, num1, num2=None):
        """
        the function returns the sub of the second number from the first
        """
        if '-' in num1:
            raise ArithmeticError("Cannot sum digits of a negative number")
        num1 = str(num1).replace(".", "")
        sum_digits = 0
        for x in num1:
            if x not in list("0123456789"):
                raise ValueError("Invalid input for this action")
            sum_digits += int(x)
        return int(sum_digits)

    def get_side(self) -> str:
        return "right"

    def get_priority(self) -> int:
        return OperatorFactory().get_priority("#")