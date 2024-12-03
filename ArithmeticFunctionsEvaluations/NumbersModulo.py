from ArithmeticFunctionsEvaluations.Operator import Operator

class NumbersModulo(Operator):
    def execute(self,num1,num2):
        """
        :param num1: number1
        :param num2: number2
        :return: returns the modulo of the number2 from the number 1
        """
        return num1%num2
