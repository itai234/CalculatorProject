import  pytest
from Evaluation.TransformInfixToPostFix import  *
converter= InfixToPostfix()

def test_Conversion():
    converter.set_expression(['3', '+', '5'])
    converter.convert()
    print(converter.get_post_fix())

