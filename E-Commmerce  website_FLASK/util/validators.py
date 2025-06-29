from datetime import datetime
from datetime import date

def validate_boolean(value):
    """
    Validates and converts a value to a boolean.

    The function checks whether the input is a valid boolean-like value. It first ensures 
    the input is not empty, then checks if it is an integer (0 or 1). If valid, it returns 
    the corresponding boolean value.

    Args:
        value: The input value to be validated. Typically expected to be 0, 1, "0", or "1".

    Returns:
        bool: `True` if the input is 1, `False` if the input is 0.

    Raises:
        ValueError: If the input is empty, not an integer, or not 0 or 1.
    """
    if str(value).strip() == "":
        raise ValueError("Boolean input cannot be empty.")
    
    try:
        value = int(value)
    except ValueError:
        raise ValueError("Boolean value must be an integer 0 or 1.")
    
    if value not in (0, 1):
        raise ValueError("Boolean value must be 0 or 1.")
    return bool(value)


def validate_date(date_str):
    """
    Validates a date string and ensures it is in the correct format and not in the past.

    This function checks if the input string is non-empty, follows the "YYYY-MM-DD" format,
    and represents a date that is not earlier than today.

    Args:
        date_str (str): The date string to validate, expected in "YYYY-MM-DD" format.

    Returns:
        datetime.date: The parsed date object if the input is valid and not in the past.

    Raises:
        ValueError: If the input is empty, not in the correct format, or if the date is in the past.
    """

    if not date_str.strip():
        raise ValueError("Date input cannot be empty.")
    try:
        parsed_date = datetime.strptime(date_str, "%Y-%m-%d").date()
        if parsed_date < date.today():
            raise ValueError("Date cannot be in the past.")
        return parsed_date
    except ValueError:
        raise ValueError("Invalid date format. Use YYYY-MM-DD.")

def validate_int(value):
        """
    Validates that the input is a non-empty, valid integer.

    This function ensures that the input is not an empty string and can be converted to an integer.

    Args:
        value: The input value to validate, expected to be convertible to an integer.

    Returns:
        int: The validated integer value.

    Raises:
        ValueError: If the input is empty or cannot be converted to an integer.
    """
        if str(value).strip() == "":
            raise ValueError("Integer input cannot be empty.")
        try:
            return int(value)
        except ValueError:
            raise ValueError("Invalid integer value.")
