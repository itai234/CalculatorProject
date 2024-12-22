
from ArithmeticFunctionsEvaluations.Properties import get_side, get_operators
from ArithmeticFunctionsEvaluations.OperatorFactory import *


class EvaluationOfPostFix:
    """
    the class handles the evaluation of the posfix expression , also
    the class is a singleton
    """
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(EvaluationOfPostFix, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        """
        initialize the properties
        """
        self._stack = []
        self._PostFixExpression = []
        self._factory = OperatorFactory()

    def set_expression(self, post_fix_expression: list):
        # sets a certain expression
        self._reset()
        self._PostFixExpression = post_fix_expression

    def _reset(self):
        # resets the properties
        self._stack = []
        self._PostFixExpression = []

    def evaluate(self,) -> float:
        """
        main function to evaluate the postfix expression
        """
        for element in self._PostFixExpression:
            if self.is_operator(element):
                self.handle_difference(element)
            else:
                self._stack.append(element)

        if self._stack[0] == float('inf'):
            raise ArithmeticError("The result is too Big.")
        return self._stack[0]
    def is_operator(self, element):
        """
        checks if the element is an operator
        """
        oplist = get_operators()
        return element in oplist

    def handle_difference(self, operator: str):
        """
        checks if the operator is a middle operator is a side operator
        means that 2 operands operators or else
        """
        if get_side(operator) == "Middle":
            self.two_operators_calculation(operator)
        else:
            self.one_operator_calculation(operator)

    def one_operator_calculation(self, operator: str):
        """
        calculator for 1 operands operators
        """
        operand1 = self._stack.pop()
        if operator == '#':
            self._stack.append(self._factory.operation(operator, str(operand1)))
        else:
            self._stack.append(self._factory.operation(operator, float(operand1)))

    def two_operators_calculation(self, operator: str):
        """
        calculate result for 2 operands operators
        """
        operand1 = self._stack.pop()
        operand2 = self._stack.pop()
        self._stack.append(self._factory.operation(operator, float(operand2), float(operand1)))
