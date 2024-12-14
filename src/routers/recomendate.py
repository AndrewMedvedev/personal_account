from fastapi import APIRouter, Request, HTTPException, status
from src.database.schemas import RecomendateModel
from src.database.models import Recomendate
from src.database.services.crud import CRUD
from src.api.controls import send_data_recomendate, token

router = APIRouter(prefix="/recomendate", tags=["recomendate"])


@router.post("/")
async def recomendate(model: RecomendateModel, request: Request):
    tkn = request.cookies.get("access")
    data = await token(tkn)
    if data != None:
        user_data = Recomendate(
            email=data,
            top_n=model.top_n,
            age=model.age,
            gender=model.gender,
            sport=model.sport,
            foreign=model.foreign,
            gpa=model.gpa,
            total_points=model.total_points,
            bonus_points=model.bonus_points,
            exams=model.exams,
            education=model.education,
            study_form=model.study_form,
        )
        await CRUD().create_data(user_data)
        recomendate = await send_data_recomendate(model)

        return recomendate["data"]
    else:
        return HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
