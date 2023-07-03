import pytest
from src.assert_examples import division, square_root, validate_email, delete_file, InvalidEmailError

def test_division_zero_division_error():
    """
    Test that a ZeroDivisionError is raised when the second argument is 0
    """
    with pytest.raises(ZeroDivisionError) as excinfo:
        division(1, 0)
    assert str(excinfo.value) == "Division by zero is not allowed"

def test_square_root_value_error():
    """
    Test that a ValueError is raised when the argument is negative
    """
    with pytest.raises(ValueError) as excinfo:
        square_root(-1)
    assert str(excinfo.value) == "Square root of negative numbers is not allowed"

def test_delete_file_not_found_error():
    """
    Test that a FileNotFoundError is raised when the file does not exist
    """
    with pytest.raises(FileNotFoundError) as excinfo:
        delete_file("non_existent_file.txt")
    assert str(excinfo.value) == "File non_existent_file.txt not found"

def test_validate_email_value_error():
    """
    Test that an InvalidEmailError is raised when the email address is invalid
    """
    with pytest.raises(InvalidEmailError) as excinfo:
        validate_email("invalid_email")
    assert str(excinfo.value) == "Invalid email address"

def test_division_no_exception_raised():
    """
    Test that no exception is raised when the second argument is not 0
    """
    try:
        division(1, 1)
    except Exception as excinfo:
        pytest.fail(f"Unexpected exception raised: {excinfo}")

def test_square_root_no_exception_raised():
    """
    Test that no exception is raised when the argument is not negative
    """
    try:
        square_root(1)
    except Exception as excinfo:
        pytest.fail(f"Unexpected exception raised: {excinfo}")

def test_square_root_division_multiple_exceptions():
    """
    Test that multiple exceptions can be asserted in a single test
    """
    with pytest.raises((ValueError, ZeroDivisionError)) as excinfo:
        square_root(-1)
    assert str(excinfo.value) == "Square root of negative numbers is not allowed"






