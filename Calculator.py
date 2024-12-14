import time
from Evaluation.EvaluatePostFixExpression import EvaluationOfPostFix
from ReformattingEquation.Reformater import Reformat
from Evaluation.TransformInfixToPostFix import InfixToPostfix
from Timer import evaluate_with_timeout, TimeoutError


def main():
    InfixConverter = InfixToPostfix()
    print("\n" + "="*50)
    print("💻  Welcome to My Advanced Calculator! 🧮")
    print("="*50 + "\n")
    print("Instructions:")
    print("- Enter mathematical equations in standard notation (e.g., 3 + 4 * 2 / (1 - 5) ^ 2).")
    print("- Use 'EXIT' to close the calculator.")
    print("- Supports advanced operations, unary negatives, and parentheses.\n")
    print("- Calculations have a time limit of 5 seconds.\n")

    while True:
        try:
            print("-" * 50)
            equation = input("🔢 Enter Your Equation: ")
            if equation.strip().upper() == "EXIT":
                print("\nThank you for using the calculator! Goodbye! 👋")
                exit(0)

            start_time = time.time()
            equation = list(Reformat(equation))
            InfixConverter.setExpression(equation)
            InfixConverter.convert()
            PostFix = InfixConverter.getPostFix()
            evaluator = EvaluationOfPostFix()
            evaluator.setExpression(PostFix)

            result = evaluate_with_timeout(evaluator, timeout=5)
            elapsed_time = time.time() - start_time

            print(f"✅ Result: {result} (calculated in {elapsed_time:.2f} seconds)")

        except TimeoutError as te:
            print(f"⏰ Timeout: {te}")
        except Exception as e:
            print(f"⚠️ Error: {e}")
            print("Please try again with a valid equation!")


if __name__ == "__main__":
    main()
