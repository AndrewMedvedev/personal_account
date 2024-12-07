from fastapi import APIRouter, Request, Response, HTTPException, status
from src.database.schemas import PersonalDataModel, RecomendateModel
from src.database.services.crud import CRUD
from src.database.services.controls import JWTControl
from src.database.models import PersonalData, Recomendate

router = APIRouter(prefix="/user_data", tags=["user_data"])


@router.post("/post_personal")
async def post_personal_data(model: PersonalDataModel, request: Request):
    token = request.cookies.get("access")
    data = await JWTControl.token(token)
    user_model = PersonalData(
        email=data,
        first_name=model.first_name,
        last_name=model.last_name,
        dad_name=model.dad_name,
        bio=model.bio,
        school=model.school,
    )
    await CRUD().create_data(user_model)
    return HTTPException(status_code=status.HTTP_200_OK)


@router.get("/get_personal")
async def get_personal_data(request: Request):
    token = request.cookies.get("access")
    data = await JWTControl.token(token)
    get = await CRUD().read_data(PersonalData, email=data)
    if get is not None:
        return get
    return HTTPException(status_code=status.HTTP_404_NOT_FOUND)


# @router.put('/recomendate')
# async def put_recomendate()
