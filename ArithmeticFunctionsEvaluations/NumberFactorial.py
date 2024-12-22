
from ArithmeticFunctionsEvaluations.Operator import Operator


class NumberFactorial(Operator):
    def execute(self, num1, num2=None):
        """
        :param num: operand
        :return: the factorial of the number given
        """
        if num1 < 0 or not type(num1) == float:
            raise ArithmeticError("Factorial is only for the positive integers")
        if isinstance(num1, float):
            if num1.is_integer():
                num1 = int(num1)
            else:
                raise ArithmeticError("Cannot perform Factorial on non-integer float numbers")
        elif not isinstance(num1, int):
            raise ValueError("Factorial is only for integers")
        if num1 > 170:
            raise OverflowError("Cannot perform factorial on very large numbers. ")
        result = 1
        for i in range(1, num1 + 1):
            result *= i
        return result

    def get_side(self) -> str:
        return "right"


