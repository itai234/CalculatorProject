from ArithmeticFunctionsEvaluations.NumberUnaryMinus import NumberUnaryMinus
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
from ArithmeticFunctionsEvaluations.NumberSumDigits import NumberSumDigits


class OperatorFactory:
    """
    this factory will have all the operators classes evaluations performed by him
    it will have his dict of operators that each has the value of the class of the operator and will perform
    the calculations
    """
    _instance = None
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(OperatorFactory, cls).__new__(cls)
        return cls._instance

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
            '!': NumberFactorial,
            '#': NumberSumDigits,
            'Unary':NumberUnaryMinus
        }
        self._Priorities = {
            '+': 1,
            '-': 1,
            '*': 2,
            '/': 2,
            '^': 3,
            '%': 4,
            '$': 5,
            '&': 5,
            '@': 5,
            '~': 6,
            '!': 6,
            '#': 6,
            'Unary':2.5
        }

    def Operation(self, operatorType, num1, num2=None) -> float:
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

    def getOperators(self) -> list:
        return list(self._operators.keys())
    def getNumbers(self) ->list:
        return list("0123456789")
    def getParenthesis(self)-> list:
        return list("()")
    def getFloatingPoint(self)->list:
        return list(".")
    def getOpeningParenthesis(self)->list:
        return list("(")
    def getClosingParenthesis(self) -> list:
        return list(")")
    def getTwoOperandsOperators(self)-> list:
        return list("+-*/^%$&@")
    def getOneOperandsOperators(self) -> list:
        return list("#~!")
    def getPriority(self,Operator:str)->int:
        return self._Priorities.get(Operator)
    def getSide(self, operator: str) -> str:
        operator_class = self._operators.get(operator)
        if operator_class is None:
            raise ValueError(f"Operator '{operator}' is not defined.")
        return operator_class().getSide()
    def getParenthesisPairs(self) ->dict:
        return {'(':')'}
    def getAllLegalLetters(self)->list:
        return list(self.getOperators()+ self.getNumbers()+ self.getParenthesis()+ self.getFloatingPoint())
