from ArithmeticFunctionsEvaluations.Properties import OPERATORS


class OperatorFactory:
    """
    this factory will have all the operators classes evaluations performed by him
    it will have his dict of operators that each has the value of the class of the operator and will perform
    the calculations.
    the factory is a singleton
    """
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(OperatorFactory, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        # has a operators dict with references to their classes
        # and a dict of the operators with their properties
        if not hasattr(self, "_initialized"):
            self._operators = OPERATORS
            self._initialized = True

    def operation(self, operator_type, num1, num2=None) -> float:
        """
        this function performs the calculation , it receives the operator type like +, - and more ,
        it gets two numbers but if receives one number then the other is None by default (if the user wants Factorial
        or Neg) and it calls the relevant function .
        """
        return self._operators.get(operator_type)().execute(num1, num2)
