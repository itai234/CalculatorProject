from ArithmeticFunctionsEvaluations.EdgeResults import MAX_RESULT, MINIMUM_TO_ZERO
from ArithmeticFunctionsEvaluations.Operator import Operator


class NumbersDivision(Operator):
    def execute(self, num1, num2):
        """
        the function returns the result of the division of the first number by the second
        """
        if num2 == 0:
            raise ZeroDivisionError("You cannot divide a number by zero")

        try:
            result = num1 / num2
            if abs(result) < MINIMUM_TO_ZERO:
                return 0
            if abs(result) > MAX_RESULT:
                raise OverflowError("Result is too large to compute.")
            return result
        except OverflowError:
            raise OverflowError("The result of the division is too large.")
        except Exception as e:
            raise Exception(f"unexpected error: {e}")

    def get_side(self) -> str:
        return "Middle"

