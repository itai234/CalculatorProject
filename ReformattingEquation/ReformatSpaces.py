def fix_spaces_in_equation(equation: str) -> str:
    """
    the function fixes the white spaces in the equation and tabs
    """
    return equation.replace(" ", "").replace("\t", "").replace("\n", "")
