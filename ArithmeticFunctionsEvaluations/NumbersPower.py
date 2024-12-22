from math import pow

from ArithmeticFunctionsEvaluations.EdgeResults import MAX_RESULT, MINIMUM_TO_ZERO
from ArithmeticFunctionsEvaluations.Operator import Operator


class NumbersPower(Operator):
    def execute(self, num1, num2)->float:
        """
        :param num1: first number
        :param num2: second number
        :return: first number power by the second number
        """
        if num1 < 0 and (num2 < 1 and num2 > -1):
            raise ArithmeticError("Cannot Perform sqrt on a negative value")
        if num1 == 0 and num2 <= 0:
            raise ArithmeticError("0 raised to a non-positive power is undefined.")
        try:
            result = pow(num1, num2)
            if result > MAX_RESULT:
                raise OverflowError("Result too large to compute.")
            if result < MINIMUM_TO_ZERO:
                return 0
            return result
        except OverflowError:
            raise OverflowError("Result too large to compute.")
        except ValueError:
            raise ValueError("Cannot Perform sqrt on a negative value!")

    def get_side(self) -> str:
        return "Middle"

