

class EquationValidationError(Exception):
    def __init__(self, errors):
        """
        this is the custom exceptions class that will throw the errors list .
        """

        self._errors = list(dict.fromkeys(errors))
        message = "\n".join(self._errors)
        super().__init__(f"Evaluation failed, reasons : \n{message}")
