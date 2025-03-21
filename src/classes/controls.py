import base64
import hashlib
import logging
import os


async def create_codes() -> dict:
    code_verifier = (
        base64.urlsafe_b64encode(os.urandom(64)).rstrip(b"=").decode("utf-8")
    )
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
