from fastapi import HTTPException, status
from src.classes.tokens_classes import SendTokens
from src.database.models import PersonalData
from src.database.services.crud import CRUD


class UserData:

    def __init__(
        self,
        token_access: str,
        token_refresh: str,
        model=None,
    ) -> None:
        self.token_access = token_access
        self.token_refresh = token_refresh
        self.model = model

    async def post_personal_data(self) -> HTTPException:
        tkn_access = await SendTokens(self.token_access).send_access_token()
        tkn_refresh = await SendTokens(self.token_refresh).send_refresh_token()
        if tkn_access != False and tkn_refresh != False:
            user_model = PersonalData(
                email=tkn_access,
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
        tkn_access = await SendTokens(self.token_access).send_access_token()
        tkn_refresh = await SendTokens(self.token_refresh).send_refresh_token()
        if tkn_access != False and tkn_refresh != False:
            await CRUD().update_data_email(
                model=PersonalData,
                new_model=self.model,
                email=tkn_access,
            )
            return HTTPException(status_code=status.HTTP_200_OK)
        else:
            return HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)

    async def get_personal_data(self) -> dict | HTTPException:
        tkn_access = await SendTokens(self.token_access).send_access_token()
        tkn_refresh = await SendTokens(self.token_refresh).send_refresh_token()
        if tkn_access != False and tkn_refresh != False:
            return await CRUD().read_data(
                PersonalData,
                email=tkn_access,
            )
        else:
            return HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
