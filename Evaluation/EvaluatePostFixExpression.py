from ArithmeticFunctionsEvaluations.OperatorFactory import OperatorFactory


class EvaluationOfPostFix:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(EvaluationOfPostFix, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        self._stack = []
        self._PostFixExpression = []
        self._factory = OperatorFactory()

    def setExpression(self, PostFixExpression: list):
        self._reset()
        self._PostFixExpression = PostFixExpression
    def _reset(self):
        self._stack = []
        self._PostFixExpression = []

    def evaluate(self,) -> float :

        for element in self._PostFixExpression:
            if self.isOperator(element):
                self.handleDifference(element)
            else:
                self._stack.append(element)
        return self._stack[0]

    def isOperator(self,element):
        oplist = self._factory.getOperators()
        return element in oplist
    def handleDifference(self,operator:str):
        if self._factory.getSide(operator) == "Middle":
            self.twoOperatorsCalculation(operator)
        else:
            self.oneOperatorCalculation(operator)
    def oneOperatorCalculation(self,operator:str):
        operand1 = self._stack.pop()
        self._stack.append(self._factory.Operation(operator,float(operand1)))
    def twoOperatorsCalculation(self,operator:str):
        operand1 = self._stack.pop()
        operand2 = self._stack.pop()
        self._stack.append(self._factory.Operation(operator,float(operand2),float(operand1)))






