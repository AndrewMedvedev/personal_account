from fastapi import HTTPException, Response, status
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

    async def post_personal_data(self) -> HTTPException:
        check_tokens = check(
            access=self.token_access,
            refresh=self.token_refresh,
        )
        if type(check_tokens) == dict:
            user_model = PersonalData(
                email=check_tokens.get("email"),
                first_name=self.model.first_name,
                last_name=self.model.last_name,
                dad_name=self.model.dad_name,
                bio=self.model.bio,
            )
            self.response.set_cookie(
                key="access",
                value=check_tokens.get("access"),
            )
            await CRUD().create_data(user_model)
            return HTTPException(status_code=status.HTTP_200_OK)
        elif type(check_tokens) == str:
            user_model = PersonalData(
                email=check_tokens,
                first_name=self.model.first_name,
                last_name=self.model.last_name,
                dad_name=self.model.dad_name,
                bio=self.model.bio,
            )
            await CRUD().create_data(user_model)
            return HTTPException(status_code=status.HTTP_200_OK)
        else:
            return HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)

    async def put_personal_data(self) -> HTTPException:
        check_tokens = check(
            access=self.token_access,
            refresh=self.token_refresh,
        )
        if type(check_tokens) == dict:
            await CRUD().update_data_email(
                model=PersonalData,
                new_model=self.model,
                email=check_tokens.get("email"),
            )
            self.response.set_cookie(
                key="access",
                value=check_tokens.get("access"),
            )
            return HTTPException(status_code=status.HTTP_200_OK)
        elif type(check_tokens) == str:
            await CRUD().update_data_email(
                model=PersonalData,
                new_model=self.model,
                email=check_tokens,
            )
            return HTTPException(status_code=status.HTTP_200_OK)
        else:
            return HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)

    async def get_personal_data(self) -> dict | HTTPException:
        check_tokens = check(
            access=self.token_access,
            refresh=self.token_refresh,
        )
        if type(check_tokens) == dict:
            self.response.set_cookie(
                key="access",
                value=check_tokens.get("access"),
            )
            return await CRUD().read_data(
                PersonalData,
                email=check_tokens.get("email"),
            )
        elif type(check_tokens) == str:
            return await CRUD().read_data(
                PersonalData,
                email=check_tokens,
            )
        else:
            return HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
