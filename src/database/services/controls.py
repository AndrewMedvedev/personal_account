from fastapi import HTTPException, status, Response
from jose import jwt
from jose.exceptions import JWTError
from src.config import Settings as setting


class JWTControl:

    @staticmethod
    async def token(token):
        if not token:
            return HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
        else:
            try:
                access = jwt.decode(
                    token, setting.SECRET_KEY, algorithms=setting.ALGORITHM
                )
                if "user_name" not in access and "mode" not in access:
                    return HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
                if access["mode"] != "access_token":
                    return HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
                return access["user_name"]
            except JWTError:
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                )
