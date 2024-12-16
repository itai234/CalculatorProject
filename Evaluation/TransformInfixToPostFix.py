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

    def set_expression(self, infix_expression: list):
        self._reset()
        self._InfixExpression = infix_expression

    def _reset(self):
        self._stack = []
        self._PostFixExpression = []
        self._prev = None

    def convert(self):
        i = 0
        for element in self._InfixExpression:
            self._prev = i-1
            if self.check_if_operand(element):
                self.handle_operand(element)
            elif self.check_if_operator(element):
                if element == '-':
                    self.handle_minus()
                else:
                    self.handle_operator(element)
            elif element in self._factory.get_opening_parenthesis():
                self.handle_opening_parenthesis()
            elif element in self._factory.get_closing_parenthesis():
                self.handle_closing_parenthesis()
            i += 1
        self.clear_remaining_operators()

    def handle_operand(self, element):
        self._PostFixExpression.append(element)

    def handle_operator(self, element):
        while (self._stack and self._stack[-1] != (self._factory.get_opening_parenthesis()[0]) and
               self._factory.get_priority(self._stack[-1]) >= self._factory.get_priority(element)):
            self._PostFixExpression.append(self._stack.pop())
        self._stack.append(element)

    def handle_opening_parenthesis(self):
        self._stack.append(self._factory.get_opening_parenthesis()[0])

    def handle_closing_parenthesis(self):
        while self._stack and self._stack[-1] != self._factory.get_opening_parenthesis()[0]:
            self._PostFixExpression.append(self._stack.pop())
        if self._stack and self._stack[-1] == self._factory.get_opening_parenthesis()[0]:
            self._stack.pop()

    def clear_remaining_operators(self):
        while self._stack:
            self._PostFixExpression.append(self._stack.pop())

    def check_if_operator(self, element) -> bool:
        return element in self._factory.get_operators()

    def handle_minus(self):
        if self.check_unary_minus():
            while (self._stack and self._stack[-1] != self._factory.get_opening_parenthesis()[0] and
                   self._factory.get_priority(self._stack[-1]) >= self._factory.get_priority('Unary')):
                self._PostFixExpression.append(self._stack.pop())
            self._stack.append('Unary')
        else:
            self.handle_operator('-')

    def check_unary_minus(self):
        operators = set(OperatorFactory().get_operators())
        operators.remove('!')
        operators.remove('#')
        return (
                self._prev < 0 or  # At the start of the expression
                self._InfixExpression[self._prev] in operators or
                self._InfixExpression[self._prev] in self._factory.get_opening_parenthesis()
        )

    def check_if_operand(self, element: str) -> bool:
        if element == '-':
            return False
        valid_chars = self._factory.get_numbers() + self._factory.get_floating_point() + ['-']
        return all(char in valid_chars for char in element)

    def get_post_fix(self):
        return self._PostFixExpression
