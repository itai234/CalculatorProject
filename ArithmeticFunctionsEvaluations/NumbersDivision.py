from ArithmeticFunctionsEvaluations.Operator import Operator
from ArithmeticFunctionsEvaluations.Properties import *


class NumbersDivision(Operator):
    def execute(self, num1, num2):
        """
        the function returns the result of the division of the first number by the second
        """
        if num2 == 0:
            raise ZeroDivisionError("You cannot divide a number by zero")

        try:
            result = num1 / num2
            if abs(result) < 10**-10:
                return 0
            if abs(result) > 10**10000:
                raise OverflowError("Result is too large to compute.")
            return result
        except OverflowError:
            raise OverflowError("The result of the division is too large.")
        except Exception as e:
            raise Exception(f"unexpected error: {e}")

    def get_side(self) -> str:
        return "Middle"

    def get_priority(self) -> int:
        return get_priority("/")