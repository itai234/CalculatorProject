from ReformattingEquation.Reformater import Reformat
from Evaluation.TransformInfixToPostFix import *
InfixConverter = InfixToPostfix()
print("\n\n\nWelcome To My Calculator!\n")
while(True):
    try:
        equation = input("Please Enter Your Equation, If You Wish To Stop, Write --Exit-- , Enter Your Equation: " )
        if equation.upper() == "EXIT":
            exit(0)
        else:
            equation = list(Reformat(equation))
            InfixConverter.setExpression(equation)
            InfixConverter.convert()
            PostFix = InfixConverter.getPostFix()
            print(equation)
            print(PostFix)
    except  Exception as e :
        print(e)








