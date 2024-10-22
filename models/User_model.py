from mongoengine import Document, StringField, BooleanField, ValidationError, NotUniqueError
from werkzeug.security import generate_password_hash, check_password_hash
from validation.validator_field import validate_email, validate_name, validate_password

"""
User Model:

This model represents a user in the system. It includes fields for user details such as first name, last name, email, 
and a hashed password. The model provides functionality to hash and validate passwords, ensuring secure storage. 
Additionally, the model contains email validation status, which is a boolean flag to track whether the user 
has verified their email address.

Fields:
- firstname (str): User's first name, must be alphabetic and validated by a custom regex.
- lastname (str): User's last name, must be alphabetic and validated by a custom regex.
- email (str): User's email, must follow a standard email format, unique for each user in the database.
- password_hash (str): Hashed password of the user (the password is not stored in plaintext).
- email_validated (bool): A flag that indicates if the user's email has been validated.

Methods:
- set_password: Validates and hashes a password before storing it.
- check_password: Compares a given password with the stored hash to verify correctness.
"""

class User(Document):
    # User's first name, must be alphabetic, spaces and hyphens are allowed.
    firstname = StringField(required=True, max_length=50, validation=validate_name)
    
    # User's last name, must be alphabetic, spaces and hyphens are allowed.
    lastname = StringField(required=True, max_length=50, validation=validate_name)
    
    # User's email address, must be unique and follow valid email format.
    email = StringField(required=True, unique=True, validation=validate_email)
    
    # Hashed password stored securely (plain passwords are not saved in the database).
    password_hash = StringField(required=True)
    
    # Boolean field that tracks whether the user has validated their email.
    email_validated = BooleanField(default=False)

    def set_password(self, password):
        """
        Validates and securely hashes the provided password.

        This method first ensures the password meets the required complexity (at least 6 characters, 
        containing uppercase, lowercase, and special characters). If valid, the password is hashed 
        using a secure hashing algorithm (via `werkzeug.security.generate_password_hash`), 
        ensuring the plaintext password is never stored directly.

        Parameters:
        password (str): The plaintext password to be validated and hashed.

        Raises:
        ValidationError: If the password does not meet the required complexity.
        """
        validate_password(password)  # Validate the password's complexity
        self.password_hash = generate_password_hash(password)  # Hash and store the password securely

    def check_password(self, password):
        """
        Compares the provided plaintext password with the stored hashed password.

        This method uses `werkzeug.security.check_password_hash` to compare the stored password hash 
        with the provided password. If the password matches the stored hash, the method returns True. 
        Otherwise, it returns False.

        Parameters:
        password (str): The plaintext password to be checked.

        Returns:
        bool: True if the provided password matches the stored hash, False otherwise.
        """
        return check_password_hash(self.password_hash, password)

    @classmethod
    def create_user(cls, firstname, lastname, email, password):
        """
        Class method to create a new user in the database.

        Parameters:
        - firstname (str): User's first name.
        - lastname (str): User's last name.
        - email (str): User's email address.
        - password (str): User's password.

        Returns:
        User: The newly created user object.

        Raises:
        ValidationError: If the user data is invalid or the email already exists.
        """
        try:
            user = cls(
                firstname=firstname,
                lastname=lastname,
                email=email,
                email_validated=False
            )
            user.set_password(password)
            user.save()
            return user
        except ValidationError as e:
            raise ValidationError(f"Error creating user: {str(e)}")
        except NotUniqueError:
            raise ValidationError("Email already exists. Please use a different email.")
        except Exception as e:
            raise Exception(f"An unexpected error occurred: {str(e)}")

    meta = {
        'collection': 'users',
        'indexes': [
            'email',
        ]
    }
