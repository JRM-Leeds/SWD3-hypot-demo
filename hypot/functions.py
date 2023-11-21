def addition(a, b):
    """This function return a plus b.

    :param a: interger or float number
    :type a: int or float
    :param b: the second number
    :type b: int or float
    :return: the sum of the two input numbers
    :rtype: int or float
    """
    if isinstance(a, str):
        return "Please just use integer or float"
    elif isinstance(b, str):
        return " Please just use interger or float"
    else:
        return a + b


# squared
def squared(a):
    """Calculate the square of a number

    :param a: The number to be squared
    :type a: int or float
    :return: The square of input number
    :rtype: int or float
    """

    return a * a


# sqroot
def sqroot(a):
    """_summary_

    :param a: The square root of a number
    :type a: int or float
    :return: The square root of input number
    :rtype: int or float
    """

    return a**0.5


# hypot
def hypot(a, b):
    """_summary_

    :param a: First input
    :type a: int or float
    :param b: second input
    :type b: int or float
    :return: the hypot
    :rtype: float
    """

    sa = squared(a)
    sb = squared(b)
    sumAB = addition(sa, sb)
    return sqroot(sumAB)
