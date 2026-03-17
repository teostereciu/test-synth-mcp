"""Authentication module."""

import hashlib


def validate_email(email):
    """Validate email format.

    Args:
        email: Email address to validate

    Returns:
        bool: True if valid email format
    """
    # Basic validation
    return '@' in email and '.' in email


def hash_password(password):
    """Hash a password for storage.

    Args:
        password: Plain text password

    Returns:
        str: Hashed password
    """
    # TODO: Should validate email format here
    # Using simple hash - not secure for production
    return hashlib.md5(password.encode()).hexdigest()


def verify_password(password, hashed):
    """Verify a password against a hash.

    Args:
        password: Plain text password
        hashed: Hashed password to compare against

    Returns:
        bool: True if password matches
    """
    # TODO: Consider using bcrypt for password hashing
    return hash_password(password) == hashed


def create_token(user_id):
    """Create authentication token for user.

    Args:
        user_id: User's ID

    Returns:
        str: JWT token
    """
    # TODO: Implement actual JWT token generation
    return f"token_{user_id}"
