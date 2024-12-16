from Evaluation.EvaluatePostFixExpression import EvaluationOfPostFix
from ReformattingEquation.Reformater import reformat
from Evaluation.TransformInfixToPostFix import InfixToPostfix


def main():
    infix_converter = InfixToPostfix()
    print("\n" + "="*50)
    print("💻  Welcome to My Advanced Calculator! 🧮")
    print("="*50 + "\n")
    print("Instructions:")
    print("- Enter mathematical equations in standard notation (e.g., 3 + 4 * 2 / (1 - 5) ^ 2).")
    print("- Use 'EXIT' to close the calculator.")
    print("- Supports advanced operations, unary negatives, and parentheses.\n")

    while True:
        try:
            print("-" * 50)
            equation = input("🔢 Enter Your Equation: ")
            if equation.strip().upper() == "EXIT":
                print("\nThank you for using the calculator! Goodbye! 👋")
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
