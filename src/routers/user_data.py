from fastapi import (
    APIRouter,
    Request,
    HTTPException,
    Response,
    status,
)
from src.database.schemas.personal_data_schemas import (
    PersonalDataModelUpdate,
)
from fastapi.responses import JSONResponse
from src.classes.user_data_class import UserData


router = APIRouter(prefix="/user_data", tags=["user_data"])


@router.post(
    "/add/personal",
    response_model=None,
)
async def add_personal_data(
    model: PersonalDataModelUpdate,
    request: Request,
    response: Response,
) -> dict | HTTPException:
    try:
        access = request.cookies.get("access")
        refresh = request.cookies.get("refresh")
        return await UserData(
            token_access=access,
            token_refresh=refresh,
            model=model,
            response=response,
        ).add_or_update_data_email()
    except Exception as e:
        return JSONResponse(
            status_code=status.HTTP_401_UNAUTHORIZED,
            content={"detail": str(e)},
        )


@router.get(
    "/get/personal",
    response_model=None,
)
async def get_personal_data(
    request: Request,
    response: Response,
) -> dict | HTTPException:
    try:
        access = request.cookies.get("access")
        refresh = request.cookies.get("refresh")
        return await UserData(
            token_access=access,
            token_refresh=refresh,
            response=response,
        ).get_personal_data()
    except Exception as e:
        return JSONResponse(
            status_code=status.HTTP_401_UNAUTHORIZED,
            content={"detail": str(e)},
        )
