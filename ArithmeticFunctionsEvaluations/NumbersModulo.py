from ArithmeticFunctionsEvaluations.Operator import Operator


class NumbersModulo(Operator):
    def execute(self, num1, num2):
        """
        :param num1: number1
        :param num2: number2
        :return: returns the modulo of the number2 from the number 1
        """
        if num2 == 0:
            raise ZeroDivisionError("You cannot Modulo a number by zero")
        return num1 % num2

    def get_side(self) -> str:
        return "Middle"


