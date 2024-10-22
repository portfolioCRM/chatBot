import re
from mongoengine.errors import ValidationError
from validation.regex import EMAIL_REGEX, NAME_REGEX, PASSWORD_REGEX

"""
Module: Validation Utilities for User Input

This module contains utility functions to validate user inputs such as names, emails, and passwords.
Each function leverages regular expressions (regex) to ensure that the input adheres to the expected format.

Imported Variables:
- EMAIL_REGEX: A regular expression pattern that matches a valid email format.
- NAME_REGEX: A regular expression pattern that ensures names contain only alphabetic characters, spaces, or hyphens.
- PASSWORD_REGEX: A regular expression pattern that ensures passwords meet minimum security criteria.
"""

def validate_name(_name):
    """
    Validates the given name to ensure it contains only alphabetic characters, spaces, or hyphens.

    The validation is performed using the following criteria:
    - The name can only contain letters (both uppercase and lowercase).
    - Spaces and hyphens are allowed, but they must be used between alphabetic characters (i.e., no leading or trailing spaces/hyphens).

    Parameters:
    _name (str): The name to be validated.

    Raises:
    ValidationError: If the name contains characters other than letters, spaces, or hyphens, 
    or if spaces/hyphens are used incorrectly.

    Example:
    - Valid names: "John", "Mary-Anne", "John Doe"
    - Invalid names: "John123", "Mary@", "John-"
    """
    if not re.match(NAME_REGEX, _name):
        raise ValidationError("Name must contain only alphabetic characters, spaces, or hyphens.")


def validate_email(_email):
    """
    Validates the format of the given email address using regex.

    The validation follows the general structure of a valid email address:
    - It must contain a local part (before the "@" symbol).
    - It must have an "@" symbol separating the local part and domain.
    - The domain part should have a valid domain name followed by a period (.) and a domain suffix (e.g., .com, .org).

    Parameters:
    _email (str): The email address to be validated.

    Raises:
    ValidationError: If the email does not follow a valid format.

    Example:
    - Valid emails: "example@domain.com", "user.name@sub.domain.org"
    - Invalid emails: "example@domain", "user@domain..com"
    """
    if not re.match(EMAIL_REGEX, _email):
        raise ValidationError("Invalid email format.")


def validate_password(_password):
    """
    Validates the complexity of the given password using regex.

    The password must meet the following criteria:
    - It must be at least 6 characters long.
    - It must contain at least one uppercase letter.
    - It must contain at least one lowercase letter.
    - It must contain at least one special character (non-alphanumeric, such as !, @, #, etc.).

    Parameters:
    _password (str): The password to be validated.

    Raises:
    ValidationError: If the password does not meet the complexity requirements.

    Example:
    - Valid passwords: "Password1!", "Strong@2021"
    - Invalid passwords: "pass", "Password", "123456"
    """
    if not re.match(PASSWORD_REGEX, _password):
        raise ValidationError("Password must be at least 6 characters long, contain at least one uppercase letter, one lowercase letter, and one special character.")
