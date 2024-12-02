from math import pow
class ArithmeticCalculations:
    """
    class to handle all the arithmetic calculations.
    """
    def AddNumbers(self,num1,num2):
        """
        the function returns the sum of the two numbers given to it
        """
        return num1+num2

    def SubNumbers(self, num1, num2):
        """
        the function returns the sub of the second number from the first
        """
        return num1 - num2

    def MulNumbers(self, num1, num2):
        """
        the function returns the result of the muliplication of the two numbers
        """
        return num1 * num2

    def DivNumbers(self, num1, num2):
        """
        the function returns the result of the division of the first number by the second
        """
        if num2 == 0 :
            raise ZeroDivisionError("You cannot divide a number by zero")
        return num1 / num2
    def PowNumbers(self,num1,num2):
        """
        :param num1: first number
        :param num2: second number
        :return: first number power by the second number
        """
        return pow(num1,num2)
    def ModulNumbers(self,num1,num2):
        """
        :param num1: number1
        :param num2: number2
        :return: returns the modulue of the number2 from the number 1
        """
        return num1%num2

    def MaxNumbers(self,num1,num2):
        """
        :param num1: operand1
        :param num2: operand2
        :return: return the maximum of the operands
        """
        if num1>num2:
            return num1
        return num2

    def MinNumbers(self, num1, num2):
        """
        :param num1: operand1
        :param num2: operand2
        :return: return the minimum of the operands
        """
        if num1 > num2:
            return num2
        return num1
    def AvgNumbers(self, num1, num2):
        """
        :param num1: operand1
        :param num2: operand2
        :return: return the averege of the operands
        """
        return (num1 + num2)/2

    def NegNumber(self, num1):
        """
        :param num1: operand
        :return: return the opposite sign number
        """
        return -num1
    def factorialNumber(self,num):
        """
        :param num: operand
        :return: the factorial of the number given
        """
        if num<0 or not type(num) == int :
            raise ValueError("Factorial is only for the positive integers")
        result =1
        for i in range(1,num+1):
            result*=i
        return result




