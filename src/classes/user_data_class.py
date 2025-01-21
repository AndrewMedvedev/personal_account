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
        check = check(
            access=self.token_access,
            refresh=self.token_refresh,
        )
        if type(check) == dict:
            user_model = PersonalData(
                email=check.get("email"),
                first_name=self.model.first_name,
                last_name=self.model.last_name,
                dad_name=self.model.dad_name,
                bio=self.model.bio,
            )
            self.response.set_cookie(
                key="access",
                value=check.get("access"),
            )
            await CRUD().create_data(user_model)
            return HTTPException(status_code=status.HTTP_200_OK)
        elif type(check) == str:
            user_model = PersonalData(
                email=check,
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
        check = check(
            access=self.token_access,
            refresh=self.token_refresh,
        )
        if type(check) == dict:
            await CRUD().update_data_email(
                model=PersonalData,
                new_model=self.model,
                email=check.get("email"),
            )
            self.response.set_cookie(
                key="access",
                value=check.get("access"),
            )
            return HTTPException(status_code=status.HTTP_200_OK)
        elif type(check) == str:
            await CRUD().update_data_email(
                model=PersonalData,
                new_model=self.model,
                email=check,
            )
            return HTTPException(status_code=status.HTTP_200_OK)
        else:
            return HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)

    async def get_personal_data(self) -> dict | HTTPException:
        check = check(
            access=self.token_access,
            refresh=self.token_refresh,
        )
        if type(check) == dict:
            self.response.set_cookie(
                key="access",
                value=check.get("access"),
            )
            return await CRUD().read_data(
                PersonalData,
                email=check.get("email"),
            )
        elif type(check) == str:
            return await CRUD().read_data(
                PersonalData,
                email=check,
            )
        else:
            return HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
