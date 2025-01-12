from fastapi import APIRouter, Request, HTTPException, status
from src.database.services.crud import CRUD
from src.database.schemas import PersonalDataModelUpdate, PersonalDataModel
from src.api.controls import token
from src.database.models import PersonalData

router = APIRouter(prefix="/user_data", tags=["user_data"])


@router.post("/post/personal")
async def post_personal_data(model: PersonalDataModel, request: Request):
    tkn = request.cookies.get("access")
    data = await token(tkn)
    if data != None:
        if type(data) != int:
            user_model = PersonalData(
                phone_number=model.phone_number,
                email=data,
                first_name=model.first_name,
                last_name=model.last_name,
                dad_name=model.dad_name,
                bio=model.bio,
                registration_type="DEFAULT"
            )
            await CRUD().create_data(user_model)
            return HTTPException(status_code=status.HTTP_200_OK)
        else:
            user_model = PersonalData(
                phone_number=model.phone_number,
                id_vk=data,
                first_name=model.first_name,
                last_name=model.last_name,
                dad_name=model.dad_name,
                bio=model.bio,
                registration_type="VK"
            )
            await CRUD().create_data(user_model)
            return HTTPException(status_code=status.HTTP_200_OK)

    else:
        return HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)


@router.put("/put/personal")
async def put_personal_data(model: PersonalDataModelUpdate, request: Request):
    tkn = request.cookies.get("access")
    data = await token(tkn)
    if data != None:
        if type(data) != int:
            await CRUD().update_data_email(model=PersonalData, new_model=model, email=data)
            return HTTPException(status_code=status.HTTP_200_OK)
        else:
            await CRUD().update_data_id_vk(model=PersonalData, new_model=model, id_vk=data)
            return HTTPException(status_code=status.HTTP_200_OK)
    else:
        return HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)


@router.get("/get/personal")
async def get_personal_data(request: Request):
    tkn = request.cookies.get("access")
    data = await token(tkn)
    if data != None:
        get = await CRUD().read_data(PersonalData, email=data)
        return get
    else:
        return HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
