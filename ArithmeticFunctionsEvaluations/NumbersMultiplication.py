
from ArithmeticFunctionsEvaluations.Operator import Operator
from ArithmeticFunctionsEvaluations.Properties import *


class NumbersMultiplication(Operator):
    def execute(self, num1, num2):
        """
        the function returns the result of the multiplication of the two numbers
        """
        if num1 == 0 or num2 == 0:
            return 0
        try:
            result = num1 * num2
            if abs(result) > 10 ** 100:
                raise OverflowError("Result too large to compute.")
            return result
        except OverflowError:
            raise Exception("Result too large to compute.")
        except Exception as e:
            raise Exception(f"Error: {e}")

    def get_side(self) -> str:
        return "Middle"

    def get_priority(self) -> int:
        return get_priority("*")