from ArithmeticFunctionsEvaluations.Operator import Operator

class NumbersDivision(Operator):
    def execute(self, num1, num2):
        """
        the function returns the result of the division of the first number by the second
        """
        if num2 == 0:
            raise ZeroDivisionError("You cannot divide a number by zero")
        return num1 / num2