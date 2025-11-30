"""Validation utilities for MMN blockchain."""

import base58
from typing import Tuple


class MmnValidator:
    """Validation utilities for MMN blockchain."""

    @staticmethod
    def validate_address(address: str) -> Tuple[bool, str]:
        """
        Validate blockchain address.

        Args:
            address: Blockchain address to validate

        Returns:
            Tuple of (is_valid, error_message)

        Example:
            >>> is_valid, error = MmnValidator.validate_address("address")
            >>> if not is_valid:
            ...     print(f"Error: {error}")
        """
        try:
            decoded = base58.b58decode(address)
            if len(decoded) != 32:  # ED25519_PUBLIC_KEY_LENGTH
                return False, f"Invalid address length: {len(decoded)} bytes"
            return True, ""
        except Exception as e:
            return False, f"Invalid base58 encoding: {str(e)}"

    @staticmethod
    def validate_amount(balance: str, amount: str) -> Tuple[bool, str]:
        """
        Validate transaction amount.

        Args:
            balance: Available balance (as string)
            amount: Amount to send (as string)

        Returns:
            Tuple of (is_valid, error_message)

        Example:
            >>> is_valid, error = MmnValidator.validate_amount("1000000", "500000")
            >>> if is_valid:
            ...     print("Amount is valid")
        """
        try:
            big_balance = int(balance)
            big_amount = int(amount)

            if big_amount < 0:
                return False, "Amount cannot be negative"
            if big_balance < 0:
                return False, "Balance cannot be negative"
            if big_amount > big_balance:
                return False, f"Insufficient balance: {big_balance} < {big_amount}"

            return True, ""
        except ValueError as e:
            return False, f"Invalid number format: {str(e)}"

    @staticmethod
    def validate_nonce(nonce: int) -> Tuple[bool, str]:
        """
        Validate transaction nonce.

        Args:
            nonce: Transaction nonce

        Returns:
            Tuple of (is_valid, error_message)

        Example:
            >>> is_valid, error = MmnValidator.validate_nonce(5)
            >>> assert is_valid
        """
        if nonce < 0:
            return False, "Nonce cannot be negative"
        return True, ""
