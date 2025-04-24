from typing import Any

import base64
import hashlib
import logging
import os

from .exeptions import BadRequestHTTPError, ExistsHTTPError, NoPlacesHTTPError, NotFoundHTTPError


def create_codes() -> dict:
    code_verifier = base64.urlsafe_b64encode(os.urandom(64)).rstrip(b"=").decode("utf-8")
    code_challenge = (
        base64.urlsafe_b64encode(hashlib.sha256(code_verifier.encode("utf-8")).digest())
        .rstrip(b"=")
        .decode("utf-8")
    )
    return {
        "code_verifier": code_verifier,
        "code_challenge": code_challenge,
    }


def config_logging(level=logging.INFO):
    logging.basicConfig(
        level=level,
        datefmt="%Y-%m-%d %H:%M:%S",
        format="[%(asctime)s] %(module)10s:%(lineno)-3d %(levelname)-7s - %(message)s",
    )


async def valid_answer(response: Any) -> dict:
    status = response.status
    match status:
        case 200:
            return await response.json()
        case 201:
            return None
        case 204:
            return None
        case 400:
            raise BadRequestHTTPError
        case 403:
            raise NoPlacesHTTPError
        case 404:
            raise NotFoundHTTPError
        case 409:
            raise ExistsHTTPError
