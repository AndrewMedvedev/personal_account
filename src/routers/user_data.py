from fastapi import (
    APIRouter,
    HTTPException,
)
from src.classes.user_data_class import UserData
from src.database.schemas.personal_data_schemas import (
    PersonalDataModel,
    PersonalDataModelUpdate,
)


router = APIRouter(prefix="/user_data", tags=["user_data"])


@router.post(
    "/post/personal",
    response_model=None,
)
async def post_personal_data(
    model: PersonalDataModel,
    access: str,
    refresh: str,
) -> HTTPException:
    return await UserData(
        token_access=access,
        token_refresh=refresh,
        model=model,
    ).post_personal_data()


@router.put(
    "/put/personal",
    response_model=None,
)
async def put_personal_data(
    model: PersonalDataModelUpdate,
    access: str,
    refresh: str,
) -> HTTPException:
    return await UserData(
        token_access=access,
        token_refresh=refresh,
        model=model,
    ).put_personal_data()


@router.get(
    "/get/personal",
    response_model=None,
)
async def get_personal_data(
    access: str,
    refresh: str,
) -> dict | HTTPException:
    return await UserData(
        token_access=access,
        token_refresh=refresh,
    ).get_personal_data()
