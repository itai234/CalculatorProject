from ArithmeticFunctionsEvaluations.Operator import Operator
class NumberSumDigits(Operator):
    def execute(self, num1, num2 = None):
        """
        the function returns the sub of the second number from the first
        """
        if num1<0 :
            raise ValueError("cannot sum digits of a negative number")
        sum  = 0
        for x in str(num1):
            sum+= int(x)
        return sum

