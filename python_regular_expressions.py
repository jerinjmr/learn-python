"""
Learning Python3.

Complete Python Developer in 2022: Zero to Mastery
Udemy Online Course

Advanced Python: Regular Expression
"""

# Excercise 01: Email id and Password validation
import re


def email_validation(email_id):
    """Email id validation."""
    pattern = re.compile(r'(^[a-zA-Z0-9._+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)')
    check = pattern.fullmatch(email_id)
    return bool(check)


def password_validation(password):
    """
    Password validation.

    Should have at least one number.
    Should have at least one uppercase and one lowercase character.
    Should have at least one special symbol.
    Should be between 8 to 20 characters long.
    """
    pattern = re.compile(
        r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])' +
        r'[A-Za-z\d@$!#%*?&]{8,20}$')
    check = pattern.fullmatch(password)
    return bool(check)


def main():
    """Program starts here."""
    email_id = input("Enter your email id:")
    email_check = email_validation(email_id)
    print("Valid email id" if email_check else "Invalid email id")

    password = input("Type your password:")
    password_check = password_validation(password)
    print("Password accepted" if password_check
          else "Password not accepted")


if __name__ == "__main__":
    main()
