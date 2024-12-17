from abc import ABC,abstractmethod


class Operator(ABC):
    """
    abstract class of the gereral operator that every operator will inherit and use its function.
    """
    @abstractmethod
    def execute(self, num1, num2=None):
        # this will appear in each class of the operators and
        # it will execute the action.
        pass

    @abstractmethod
    def get_side(self) -> str:
        # this will appear in each class of the operators
        pass

    @abstractmethod
    def get_priority(self) -> int:
        # this will appear in each class of the operators and give
        pass

