from ArithmeticFunctionsEvaluations.NumbersAvg import NumbersAvg
from ArithmeticFunctionsEvaluations.NumbersDivision import NumbersDivision
from ArithmeticFunctionsEvaluations.NumberNeg import NumberNeg
from ArithmeticFunctionsEvaluations.NumbersAddition import NumbersAddition
from ArithmeticFunctionsEvaluations.NumbersSubtraction import NumbersSubtraction
from ArithmeticFunctionsEvaluations.NumbersMultiplication import NumbersMultiplication
from ArithmeticFunctionsEvaluations.NumbersModulo import NumbersModulo
from ArithmeticFunctionsEvaluations.NumbersPower import NumbersPower
from ArithmeticFunctionsEvaluations.NumbersMinimum import NumbersMinimum
from ArithmeticFunctionsEvaluations.NumbersMaximum import NumbersMaximum
from ArithmeticFunctionsEvaluations.NumberFactorial import NumberFactorial


class OperatorFactory:
    """
    this factory will have all the operators classes evaluations performed by him
    it will have his dict of operators that each has the value of the class of the operator and will perform
    the calculations
    """
    def __init__(self):
        self._operators = {
            '+': NumbersAddition,
            '-': NumbersSubtraction,
            '*': NumbersMultiplication,
            '/': NumbersDivision,
            '^': NumbersPower,
            '%': NumbersModulo,
            '$': NumbersMaximum,
            '&': NumbersMinimum,
            '@': NumbersAvg,
            '~': NumberNeg,
            '!': NumberFactorial
        }

    def Operation(self, operatorType, num1, num2=None):
        """
        this function performs the calculation , it receives the operator type like +, - and more ,
        it gets two numbers but if receives one number then the other is None by defult (if the user wants Factorial
        or Neg) and it calls the relevant function .
        """
        operatorClass = self._operators.get(operatorType)
        if operatorClass is None:
            raise ValueError(f"No Such Operator as : {operatorType}")
        operatorInstance = operatorClass()
        return operatorInstance.execute(num1, num2)
