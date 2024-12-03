from ArithmeticFunctionsEvaluations.Operator import Operator

class NumbersAvg(Operator):
    def execute(self, num1, num2):
        """
        :param num1: operand1
        :param num2: operand2
        :return: return the average of the operands
        """
        return (num1 + num2) / 2
