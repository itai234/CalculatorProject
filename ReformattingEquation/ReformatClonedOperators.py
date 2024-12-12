def FixClonedOperators(equation:list) -> list :
    """
    :param equation: the input is the list of the equation(list of chars )
    :return: returns the list without cloned unnecessary operators
    """
    i = 0
    while i < len(equation) - 1:
        if equation[i] in "+" and equation[i] == equation[i + 1]:
            del equation[i+1]
        else:
            i += 1
    return equation

