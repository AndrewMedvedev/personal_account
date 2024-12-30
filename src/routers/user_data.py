from fastapi import APIRouter, Request, HTTPException, status
from src.database.services.crud import CRUD
from src.database.schemas import PersonalDataModelUpdate, PersonalDataModel
from src.api.controls import token
from src.database.models import PersonalData

router = APIRouter(prefix="/user_data", tags=["user_data"])


@router.post("/post_personal")
async def post_personal_data(model: PersonalDataModel, request: Request):
    tkn = request.cookies.get("access")
    data = await token(tkn)
    if data != None:
        user_model = PersonalData(
            email=data,
            first_name=model.first_name,
            last_name=model.last_name,
            dad_name=model.dad_name,
            bio=model.bio,
        )
        await CRUD().create_data(user_model)
        return HTTPException(status_code=status.HTTP_200_OK)
    else:
        return HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)


@router.put("/put_personal")
async def put_personal_data(model: PersonalDataModelUpdate, request: Request):
    tkn = request.cookies.get("access")
    data = await token(tkn)
    if data != None:
        await CRUD().update_data(model=PersonalData, new_model=model, email=data)
        return HTTPException(status_code=status.HTTP_200_OK)
    else:
        return HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)


@router.get("/get_personal")
async def get_personal_data(request: Request):
    tkn = request.cookies.get("access")
    data = await token(tkn)
    if data != None:
        get = await CRUD().read_data(PersonalData, email=data)
        return get
    else:
        return HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
