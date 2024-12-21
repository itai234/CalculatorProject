from Evaluation.EvaluatePostFixExpression import EvaluationOfPostFix
from ReformattingEquation.Reformater import reformat
from Evaluation.TransformInfixToPostFix import InfixToPostfix

def evaluate(equation:str):
    infix_converter = InfixToPostfix()
    equation = list(reformat(equation))
    infix_converter.set_expression(equation)
    infix_converter.convert()
    post_fix = infix_converter.get_post_fix()
    evaluator = EvaluationOfPostFix()
    evaluator.set_expression(post_fix)
    return evaluator.evaluate()

def main():
    """
    main function in the program that takes the equation, and evaluate it, if there are errors in the equation it will print them
    """
    print("\n" + "=" * 50)
    print("💻  Welcome to My Advanced Calculator! 🧮")
    print("=" * 50 + "\n")
    with open("CalculatorRules", "r", encoding="utf-8") as f:
        content = f.read()
    print(content)

    while True:
        try:
            print("-" * 50)
            equation = input("🔢 Enter Your Equation: ")
            if len(equation)>(10**3):
                raise OverflowError("Your Equation is too long, try a shorter Equation!")
            if equation.strip().upper() == "EXIT":
                print("\nThank you for using my calculator! Goodbye! 👋")
                exit(0)
            result = evaluate(equation)
            print(f"✅ Result: {result}")

        except Exception as e:
            print(f"⚠️ Error: {e}")
            print("Please try again with a valid equation!")


if __name__ == "__main__":
    main()

