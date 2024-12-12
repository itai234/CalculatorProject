

class EquationValidationError(Exception):
    def __init__(self, errors):
        """
        :param the errors is the list of all the illegal actions in the equation
        """
        self.errors = errors
        message = "\n".join(errors)
        super().__init__(f"Evaluation failed, reasons : \n{message}")
