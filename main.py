from ReformattingEquation.Reformater import Reformat

while(True):
    try:
        equation = input("please enter your equation:")
        equation = list(Reformat(equation))
        print(equation)
    except  Exception as e :
        print(e)








