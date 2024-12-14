from ArithmeticFunctionsEvaluations.OperatorFactory import OperatorFactory


class InfixToPostfix:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(InfixToPostfix, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        self._stack = []
        self._PostFixExpression = []
        self._InfixExpression = []
        self._factory = OperatorFactory()

    def setExpression(self, InfixExpression: list):
        self._stack = []
        self._PostFixExpression = []
        self._InfixExpression = InfixExpression

    def convert(self):
        for element in self._InfixExpression:
            if self.isOperand(element):
                self.handleOperand(element)
            elif self.checkIfOperator(element):
                self.handleOperator(element)
            elif element in self._factory.getOpeningParenthesis():
                self.handleOpeningParenthesis()
            elif element in self._factory.getClosingParenthesis():
                self.handleClosingParenthesis()
        self.clearRemainingOperators()

    def handleOperand(self, element):
        self._PostFixExpression.append(element)

    def handleOperator(self, element):
        while (self._stack and self._stack[-1] != (self._factory.getOpeningParenthesis()[0]) and
               self._factory.getPriority(self._stack[-1]) >= self._factory.getPriority(element)):
            self._PostFixExpression.append(self._stack.pop())
        self._stack.append(element)

    def handleOpeningParenthesis(self):
        self._stack.append(self._factory.getOpeningParenthesis()[0])

    def handleClosingParenthesis(self):
        while self._stack and self._stack[-1] != self._factory.getOpeningParenthesis()[0]:
            self._PostFixExpression.append(self._stack.pop())
        if self._stack and self._stack[-1] == self._factory.getOpeningParenthesis()[0]:
            self._stack.pop()

    def clearRemainingOperators(self):
        while self._stack:
            self._PostFixExpression.append(self._stack.pop())

    def checkIfOperator(self, element) -> bool:
        return element in self._factory.getOperators()

    def isOperand(self, element: str) -> bool:
        valid_chars = self._factory.getNumbers() + self._factory.getFloatingPoint() + ['-']
        return all(char in valid_chars for char in element)

    def getPostFix(self):
        return self._PostFixExpression

