

def sum_(x: int, y: int) -> int:
    """Sum function."""
    return x + y


def sub(x: int, y: int) -> int:
    """Substration function."""
    return x - y


def mult(x: int, y: int) -> int:
    """Multiplication function."""
    return x * y


def div(x: int, y: int) -> int:
    """Division function."""
    try:
        return x / y

    except ZeroDivisionError:
        return "Division by zero isn't possible!!"
