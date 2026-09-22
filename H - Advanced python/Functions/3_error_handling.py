def sqrt(x):
    """Returns the square root of a number."""
    try:
        return x** 0.5
    except:
        print('X must be an int or float')

sqrt(4)
sqrt("joseph")
# -------------------------------------------
def sqrt(x):
    """Returns the square root of a number."""
    try:
        return x** 0.5
    except TypeError:
        print('X must be an int or float')

sqrt(4)
sqrt("joseph")
# -------------------------------------------
def sqrt(x):
    """Returns the square root of a number."""
    if x <0:
        raise ValueError("x must be non-negative")
    try:
        return x** 0.5
    except:
        print('X must be an int or float')

sqrt(4)
sqrt("joseph")