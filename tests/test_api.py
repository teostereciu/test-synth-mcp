"""Tests for the API module."""

import pytest
from src.api import get_users, create_user, delete_user


def test_get_users():
    """Test fetching all users."""
    # TODO: Need to test the error case
    users = get_users()
    assert isinstance(users, list)


def test_create_user():
    """Test user creation."""
    user = create_user("Alice", "alice@example.com")
    assert user['name'] == "Alice"
    assert user['email'] == "alice@example.com"
    assert 'id' in user


def test_delete_user():
    """Test user deletion."""
    result = delete_user(1)
    assert result is True


def test_create_user_with_invalid_email():
    """Test user creation with invalid email."""
    # TODO: Should validate email format
    user = create_user("Bob", "invalid-email")
    assert user is not None
