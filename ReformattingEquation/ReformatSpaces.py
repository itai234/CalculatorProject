def fix_spaces_in_equation(equation: str) -> str:
    """
    the function fixes the whtie spaces in the equation
    """
    return equation.replace(" ", "").replace("\t", "").replace("\n", "")
