from abc import ABC,abstractmethod

class Operator(ABC):
    """
    abstract class of the gereral operator that every operator will inherit and use its function.
    """
    @abstractmethod
    def execute(self,num1,num2 =None):
        pass
    @abstractmethod
    def getSide(self)->str:
        pass
    @abstractmethod
    def getPriority(self)->int:
        pass