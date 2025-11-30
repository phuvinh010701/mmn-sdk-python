"""Custom exceptions for MMN SDK."""


class MmnSDKError(Exception):
    """Base exception for MMN SDK errors."""

    pass


class MmnTransactionError(MmnSDKError):
    """Transaction-related errors."""

    pass


class MmnValidationError(MmnSDKError):
    """Validation errors."""

    pass


class MmnNetworkError(MmnSDKError):
    """Network and RPC errors."""

    pass


class MmnAuthError(MmnSDKError):
    """Authentication and ZK proof errors."""

    pass
