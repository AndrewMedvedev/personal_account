from fastapi import (
    APIRouter,
    HTTPException,
    status,
)
from src.database.schemas.personal_data_schemas import (
    PersonalDataModel,
    PersonalDataModelUpdate,
)
from src.classes.user_data_class import UserData


router = APIRouter(prefix="/user_data", tags=["user_data"])


@router.post(
    "/post/personal",
    response_model=None,
)
async def post_personal_data(
    model: PersonalDataModel,
    access: str,
    refresh: str,
) -> dict | HTTPException:
    try:
        return await UserData(
            token_access=access,
            token_refresh=refresh,
            model=model,
        ).post_personal_data()
    except:
        HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)


@router.put(
    "/put/personal",
    response_model=None,
)
async def put_personal_data(
    model: PersonalDataModelUpdate,
    access: str,
    refresh: str,
) -> dict | HTTPException:
    try:
        return await UserData(
            token_access=access,
            token_refresh=refresh,
            model=model,
        ).put_personal_data()
    except:
        return HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)


@router.get(
    "/get/personal",
    response_model=None,
)
async def get_personal_data(
    access: str,
    refresh: str,
) -> dict | HTTPException:
    try:
        return await UserData(
            token_access=access,
            token_refresh=refresh,
        ).get_personal_data()
    except:
        return HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
