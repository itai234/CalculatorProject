

class EquationValidationError(Exception):
    def __init__(self, errors):
        """
        :param the errors is the list of all the illegal actions in the equation
        """

        self._errors = list(dict.fromkeys(errors))
        message = "\n".join(self._errors)
        super().__init__(f"Evaluation failed, reasons : \n{message}")
