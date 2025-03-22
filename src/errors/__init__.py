__all__ = (
    "TokenError",
    "SendError",
    "NotFoundError",
    "token_error",
    "send_error",
    "not_found_error",
)

from .errors import NotFoundError, SendError, TokenError
from .func_errors import not_found_error, send_error, token_error
