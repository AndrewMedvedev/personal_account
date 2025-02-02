from fastapi import HTTPException, status, Response
from src.classes.tokens_classes import check
from src.database.models import PersonalData
from src.database.services.crud import CRUD


class UserData:

    def __init__(
        self,
        token_access: str,
        token_refresh: str,
        response: Response,
        model=None,
    ) -> None:
        self.token_access = token_access
        self.token_refresh = token_refresh
        self.response = response
        self.model = model

    async def add_or_update_data_email(self) -> dict:
        check_tokens = await check(
            access=self.token_access,
            refresh=self.token_refresh,
        )
        await CRUD().add_or_update_data_email(
            model=PersonalData,
            new_model=self.model,
            email=check_tokens.get("email"),
        )
        result = {
            "status": HTTPException(status_code=status.HTTP_200_OK),
        }
        if "access" in check_tokens:
            self.response.set_cookie(
                key="access",
                value=check_tokens.get("access"),
                samesite="none",
                httponly=True,
                secure=True,
            )
        return result

    async def get_personal_data(self) -> dict:
        check_tokens = await check(
            access=self.token_access,
            refresh=self.token_refresh,
        )
        result = {
            "data": await CRUD().read_data(
                PersonalData,
                email=check_tokens.get("email"),
            ),
            "status": HTTPException(status_code=status.HTTP_200_OK),
        }
        if "access" in check_tokens:
            self.response.set_cookie(
                key="access",
                value=check_tokens.get("access"),
                samesite="none",
                httponly=True,
                secure=True,
            )
        return result
