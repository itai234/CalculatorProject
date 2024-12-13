
from ArithmeticFunctionsEvaluations.Operator import Operator
from ArithmeticFunctionsEvaluations.OperatorFactory import *


class NumbersMultiplication(Operator):
    def execute(self, num1, num2):
        """
        the function returns the result of the multiplication of the two numbers
        """
        return num1 * num2
    def getSide(self) -> str:
        return "Middle"

    def getPriority(self) -> int:
        return OperatorFactory().getPriority("*")