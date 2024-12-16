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

    def set_expression(self, post_fix_expression: list):
        self._reset()
        self._PostFixExpression = post_fix_expression

    def _reset(self):
        self._stack = []
        self._PostFixExpression = []

    def evaluate(self,) -> float:

        for element in self._PostFixExpression:
            if self.is_operator(element):
                self.handle_difference(element)
            else:
                self._stack.append(element)
        return self._stack[0]

    def is_operator(self, element):
        oplist = self._factory.get_operators()
        return element in oplist

    def handle_difference(self, operator: str):
        if self._factory.get_side(operator) == "Middle":
            self.two_operators_calculation(operator)
        else:
            self.one_operator_calculation(operator)

    def one_operator_calculation(self, operator: str):
        operand1 = self._stack.pop()
        self._stack.append(self._factory.operation(operator, float(operand1)))

    def two_operators_calculation(self, operator: str):
        operand1 = self._stack.pop()
        operand2 = self._stack.pop()
        self._stack.append(self._factory.operation(operator, float(operand2), float(operand1)))






