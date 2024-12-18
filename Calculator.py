from Evaluation.EvaluatePostFixExpression import EvaluationOfPostFix
from ReformattingEquation.Reformater import reformat
from Evaluation.TransformInfixToPostFix import InfixToPostfix


def main():
    """
    main function in the program that takes the equation, and evaluate it, if there are errors in the equation it will print them
    """
    infix_converter = InfixToPostfix()
    print("\n" + "="*50)
    print("💻  Welcome to My Advanced Calculator! 🧮")
    print("="*50 + "\n")
    print("Instructions:")
    print("- Enter mathematical equations in standard notation for example - (3 + 4 * 2 / (1 - 5) ^ 2).")
    print("- Write 'EXIT' to close the calculator.")
    print("- My Calculator Supports :  unary negatives, and parentheses and more.\n")
    print("+ Will sum two Operands: 5+5 🟰 10 , 10+5 🟰 15")
    print("- Will subtract one operand from the other: 5-5 🟰 0 , 10-5 🟰 5")
    print("* Will multiply two Operands: 5*2 🟰 10 ")
    print("/ Will divide two Operands: 5/2 🟰 2.5 , 5/0 🟰 X (division by zero)")
    print("% Will give the modulo of one operand from the other: 5%3 🟰 2, 5%0 🟰 X(cant give modulo of a negative value) ")
    print("$ Will give the maximum value of two Operands: 5$0 🟰 5 , 123$9 🟰 123 ")
    print("& Will give the minimum value of two Operands: 5&0 🟰 0 , 123&9 🟰 9")
    print("@ Will give the avg of two Operands: 5@2 🟰 3.5")
    print("~ Will give the negative value of a operand: ~3 🟰 -3 , ~~3 🟰 X (wont work double tilda) , ~-3 🟰 3 ")
    print("! Will give the factorial of a Operand: 3! --> 3*2*1 🟰 6 , (-3)! 🟰 X (only for positive numbers) , 3!! 🟰 (3*2*1)! 🟰 720")
    print("# Will sum the digits of a Operand : 2.3# 🟰  5 , 53# 🟰 8 , 99## 🟰 9 (first sum is 18 and then 9) ")

    while True:
        try:
            print("-" * 50)
            equation = input("🔢 Enter Your Equation: ")
            if equation.strip().upper() == "EXIT":
                print("\nThank you for using my calculator! Goodbye! 👋")
                exit(0)

            equation = list(reformat(equation))
            print(equation)
            infix_converter.set_expression(equation)
            infix_converter.convert()
            post_fix = infix_converter.get_post_fix()
            print(post_fix)
            evaluator = EvaluationOfPostFix()
            evaluator.set_expression(post_fix)
            result = evaluator.evaluate()
            print(f"✅ Result: {result}")

        except Exception as e:
            print(f"⚠️ Error: {e}")
            print("Please try again with a valid equation!")


if __name__ == "__main__":
    main()
