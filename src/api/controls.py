from jose.exceptions import JWTError

from jose import jwt
import json
import aiohttp
from src.config import Settings



async def token(token):
    if not token:
        return None
    else:
        try:
            access = jwt.decode(token, Settings.SECRET_KEY, Settings.ALGORITHM)
            if "user_name" not in access and "mode" not in access:
                return None
            if access.get("mode") != "access_token":
                return None
            return access.get("user_name")
        except JWTError:
            return None
