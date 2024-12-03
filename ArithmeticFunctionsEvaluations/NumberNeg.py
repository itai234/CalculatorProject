from ArithmeticFunctionsEvaluations.Operator import Operator

class NumberNeg(Operator):
    def execute(self, num1, num2 = None):
        """
        :param num1: operand
        :return: return the opposite sign number
        """
        return -num1
