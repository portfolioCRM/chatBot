NAME_REGEX = r'^[a-zA-Z]+([ -][a-zA-Z]+)*$'
"""
NAME_REGEX:
- Matches alphabetic characters (both upper and lowercase).
- Allows optional spaces or hyphens between names.
  Examples:
  - Valid: "John", "Mary-Anne", "John Doe"
  - Invalid: "John123", "Mary@Smith"
"""

EMAIL_REGEX = r'^[\w\.-]+@[\w\.-]+\.\w+$'
"""
EMAIL_REGEX:
- Ensures a standard email format.
  Pattern breakdown:
  - `[\w\.-]+`: Matches one or more word characters (letters, digits, and underscores), dots, or hyphens.
  - `@`: Requires an "@" symbol.
  - `[\w\.-]+`: Matches the domain part (letters, digits, dots, or hyphens).
  - `\.\w+`: Ensures a period followed by at least one word character (like ".com" or ".net").
  Examples:
  - Valid: "example@domain.com", "user.name@example.co.uk"
  - Invalid: "example@domain", "user@domain..com"
"""

PASSWORD_REGEX = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*[\W_]).{6,}$'
"""
PASSWORD_REGEX:
- Enforces password complexity by requiring:
  - At least one lowercase letter.
  - At least one uppercase letter.
  - At least one special character (non-alphanumeric such as !, @, #, etc.).
  - A minimum length of 6 characters.
  Pattern breakdown:
  - `(?=.*[a-z])`: Ensures at least one lowercase letter.
  - `(?=.*[A-Z])`: Ensures at least one uppercase letter.
  - `(?=.*[\W_])`: Ensures at least one special character (any non-word character).
  - `.{6,}`: Enforces a minimum of 6 characters in total.
  Examples:
  - Valid: "Password1!", "Secret@2021"
  - Invalid: "pass", "Password", "123456"
"""