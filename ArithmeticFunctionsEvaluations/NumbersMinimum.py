from ArithmeticFunctionsEvaluations.Operator import Operator

class NumbersMinimum(Operator):
    def execute(self, num1, num2):
        """
        :param num1: operand1
        :param num2: operand2
        :return: return the minimum of the operands
        """
        if num1 > num2:
            return num2
        return num1