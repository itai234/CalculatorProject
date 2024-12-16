from abc import ABC,abstractmethod

class Operator(ABC):
    """
    abstract class of the gereral operator that every operator will inherit and use its function.
    """
    @abstractmethod
    def execute(self, num1, num2=None):
        pass

    @abstractmethod
    def get_side(self) -> str:
        pass

    @abstractmethod
    def get_priority(self) -> int:
        pass

