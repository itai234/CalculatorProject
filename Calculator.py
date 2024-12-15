from Evaluation.EvaluatePostFixExpression import EvaluationOfPostFix
from ReformattingEquation.Reformater import Reformat
from Evaluation.TransformInfixToPostFix import InfixToPostfix

def main():
    InfixConverter = InfixToPostfix()
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

            equation = list(Reformat(equation))
            print(equation)
            InfixConverter.setExpression(equation)
            InfixConverter.convert()
            PostFix = InfixConverter.getPostFix()
            print(PostFix)
            evaluator = EvaluationOfPostFix()
            evaluator.setExpression(PostFix)
            result = evaluator.evaluate()
            print(f"✅ Result: {result}")

        except TimeoutError as te:
            print(f"⏰ Timeout: {te}")
        except Exception as e:
            print(f"⚠️ Error: {e}")
            print("Please try again with a valid equation!")


if __name__ == "__main__":
    main()
