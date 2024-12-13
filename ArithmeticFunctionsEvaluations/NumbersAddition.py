from ArithmeticFunctionsEvaluations.Operator import Operator
from ArithmeticFunctionsEvaluations.OperatorFactory import *


class NumbersAddition(Operator):
    def execute(self, num1, num2):
        """
        the function returns the sum of the two numbers given to it
        """
        return num1 + num2

    def getSide(self) -> str:
        return "Middle"

    def getPriority(self) -> int:
        return OperatorFactory().getPriority("+")
