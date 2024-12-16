
from ArithmeticFunctionsEvaluations.Operator import Operator
from ArithmeticFunctionsEvaluations.OperatorFactory import *


class NumberFactorial(Operator):
    def execute(self, num1, num2=None):
        """
        :param num: operand
        :return: the factorial of the number given
        """
        if num1 < 0 or not type(num1) == float:
            raise ValueError("Factorial is only for the positive integers")
        if isinstance(num1, float):
            if num1.is_integer():
                num1 = int(num1)
            else:
                raise ValueError("Cannot perform Factorial on non-integer float numbers")
        elif not isinstance(num1, int):
            raise ValueError("Factorial is only for integers")

        result = 1
        iteration_limit = 10 ** 6
        iteration_counter = 0
        for i in range(1, num1 + 1):
            result *= i
            iteration_counter += 1
            if iteration_counter > iteration_limit:
                raise Exception("Cannot perform factorial on very large numbers. Computation taking too long.")
            if result > 10 ** 10000:
                raise Exception("Result too large to compute factorial for this number.")
        return result

    def get_side(self) -> str:
        return "right"

    def get_priority(self) -> int:
        return OperatorFactory().get_priority("!")

