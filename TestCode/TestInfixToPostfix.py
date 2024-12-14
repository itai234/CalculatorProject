import  pytest
from Evaluation.TransformInfixToPostFix import  *
converter= InfixToPostfix()

def test_Conversion():
    converter.setExpression(['3','+','5'])
    converter.convert()
    print(converter.getPostFix())

