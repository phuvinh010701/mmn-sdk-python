"""Utility functions for MMN SDK."""

from typing import Union


def format_amount(amount: Union[int, str], decimals: int = 6) -> str:
    """
    Format amount with decimal point for display.

    Args:
        amount: Amount in smallest unit (e.g., 1000000)
        decimals: Number of decimals (default: 6)

    Returns:
        Formatted string (e.g., "1.000000")

    Example:
        >>> format_amount(1500000, 6)
        '1.500000'
    """
    amount_int = int(amount)
    divisor = 10**decimals
    return f"{amount_int / divisor:.{decimals}f}"


def parse_amount(amount_str: str, decimals: int = 6) -> str:
    """
    Parse decimal amount to smallest unit.

    Args:
        amount_str: Amount as decimal string (e.g., "1.5")
        decimals: Number of decimals (default: 6)

    Returns:
        Amount in smallest unit as string (e.g., "1500000")

    Example:
        >>> parse_amount("1.5", 6)
        '1500000'
    """
    amount_float = float(amount_str)
    multiplier = 10**decimals
    return str(int(amount_float * multiplier))


def is_valid_user_id(user_id: str) -> bool:
    """
    Validate user ID format.

    Args:
        user_id: User identifier

    Returns:
        True if valid

    Example:
        >>> is_valid_user_id("user123")
        True
        >>> is_valid_user_id("")
        False
    """
    return bool(user_id and len(user_id) > 0)
