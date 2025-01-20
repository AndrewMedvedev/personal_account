from fastapi import APIRouter, Request, HTTPException
from src.classes.user_data_classes import UserData
from src.database.schemas import PersonalDataModel, PersonalDataModelUpdate


router = APIRouter(prefix="/user_data", tags=["user_data"])


@router.post(
    "/post/personal",
    response_model=None,
)
async def post_personal_data(
    model: PersonalDataModel, request: Request
) -> HTTPException:
    access = request.cookies.get("access")
    refresh = request.cookies.get("refresh")
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
    model: PersonalDataModelUpdate, request: Request
) -> HTTPException:
    access = request.cookies.get("access")
    refresh = request.cookies.get("refresh")
    return await UserData(
        token_access=access,
        token_refresh=refresh,
        model=model,
    ).put_personal_data()


@router.get(
    "/get/personal",
    response_model=None,
)
async def get_personal_data(request: Request) -> dict | HTTPException:
    access = request.cookies.get("access")
    refresh = request.cookies.get("refresh")
    return await UserData(
        token_access=access,
        token_refresh=refresh,
    ).get_personal_data()
