from Exceptions.InputExceptions import *
from ReformattingEquation.Reformater import Reformat

# doing the project assuming all the input is valid and then fixing all the exceptions
while(True):
    try:
        equation = input("please enter your equation:")
        equation = Reformat(equation)
        print(equation)
    except  Exception as e :
        print(e)








