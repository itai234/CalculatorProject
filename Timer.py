import threading
import time
class TimeoutError(Exception):
    pass
def evaluate_with_timeout(evaluator, timeout=5):
    """
    Evaluates the expression with a timeout.
    :param evaluator: An instance of the EvaluationOfPostFix class.
    :param timeout: Time limit for the calculation (in seconds).
    :return: The result of the evaluation.
    :raises TimeoutError: If the evaluation exceeds the time limit.
    """
    result_container = {"result": None, "error": None}

    def evaluate():
        try:
            result_container["result"] = evaluator.evaluate()
        except Exception as e:
            result_container["error"] = e

    evaluation_thread = threading.Thread(target=evaluate)
    evaluation_thread.start()
    evaluation_thread.join(timeout)

    if evaluation_thread.is_alive():
        # If the thread is still running, raise a timeout error
        raise TimeoutError("The calculation took too long and was stopped.\n Please Enter a different Equation")
    elif result_container["error"]:
        # If an error occurred during evaluation, raise it
        raise result_container["error"]
    return result_container["result"]
