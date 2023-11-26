def pgcd(a, b):
    """Calculates the greatest common divisor of two integers.

    Args:
        a (int): the first integer.
        b (int): the second integer.

    Returns:
        int: the PGCD of a and b.
    """
    if(b == 0):
        return a
    else:
        return pgcd(b, a % b)
