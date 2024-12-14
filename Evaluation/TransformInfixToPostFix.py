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
        self._prev = None

    def setExpression(self, InfixExpression: list):
        self._reset()
        self._InfixExpression = InfixExpression

    def _reset(self):
        self._stack = []
        self._PostFixExpression = []
        self._prev = None

    def convert(self):
        i = 0
        for element in self._InfixExpression:
            self._prev = i-1
            if self.checkIfsOperand(element):
                self.handleOperand(element)
            elif self.checkIfOperator(element):
                if element == '-':
                    self.handleMinus()
                else:
                    self.handleOperator(element)
            elif element in self._factory.getOpeningParenthesis():
                self.handleOpeningParenthesis()
            elif element in self._factory.getClosingParenthesis():
                self.handleClosingParenthesis()
            i+=1
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

    def handleMinus(self):
        if self.checkUnaryMinus():
            while (self._stack and self._stack[-1] != self._factory.getOpeningParenthesis()[0] and
                   self._factory.getPriority(self._stack[-1]) >= self._factory.getPriority('Unary')):
                self._PostFixExpression.append(self._stack.pop())
            self._stack.append('Unary')
        else:
            self.handleOperator('-')

    def checkUnaryMinus(self):
        operators = set(OperatorFactory().getOperators())
        operators.remove('!')
        operators.remove('#')
        return (
                self._prev < 0 or  # At the start of the expression
                self._InfixExpression[self._prev] in operators or
                self._InfixExpression[self._prev] in self._factory.getOpeningParenthesis()
        )

    def checkIfsOperand(self, element: str) -> bool:
        if element == '-':
            return False
        valid_chars = self._factory.getNumbers() + self._factory.getFloatingPoint() + ['-']
        return all(char in valid_chars for char in element)

    def getPostFix(self):
        return self._PostFixExpression

