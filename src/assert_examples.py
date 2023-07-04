import os
import math
import re


class InvalidEmailError(Exception):
    """
    Raised when an email address is invalid
    """

    pass


def division(a: int | float, b: int | float) -> float | ZeroDivisionError:
    """
    Returns the result of dividing a by b

    Raises:
        ZeroDivisionError: If b is 0
    """
    try:
        return a / b
    except ZeroDivisionError:
        raise ZeroDivisionError("Division by zero is not allowed")


def square_root(a: int) -> float | ValueError:
    """
    Returns the square root of a

    Raises:
        ValueError: If a is negative
    """
    try:
        return math.sqrt(a)
    except ValueError:
        raise ValueError("Square root of negative numbers is not allowed")


def delete_file(filename: str) -> None | FileNotFoundError:
    """
    Deletes a file

    Raises:
        FileNotFoundError: If the file does not exist
    """
    try:
        os.remove(filename)
    except FileNotFoundError:
        raise FileNotFoundError(f"File {filename} not found")


def validate_email(email: str) -> bool | InvalidEmailError:
    """
    Validates an email address

    Raises:
        InvalidEmailError: If the email address is invalid
    """
    if re.match(r"[^@]+@[^@]+\.[^@]+", email):
        return True
    else:
        raise InvalidEmailError("Invalid email address")
