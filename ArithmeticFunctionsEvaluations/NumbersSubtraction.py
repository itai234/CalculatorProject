from ArithmeticFunctionsEvaluations.Operator import Operator
from ArithmeticFunctionsEvaluations.OperatorFactory import *


class NumbersSubtraction(Operator):
    def execute(self, num1, num2):
        """
        the function returns the sub of the second number from the first
        """
        return num1 - num2
    def getSide(self) -> str:
        return "Middle"

    def getPriority(self) -> int:
        return OperatorFactory().getPriority("-")


