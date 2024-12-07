from fastapi import APIRouter, Request
from src.database.schemas import RecomendateModel
from src.database.models import Recomendate
from src.database.services.crud import CRUD
from src.recomendate.controls_recomendate import send_data
router = APIRouter(prefix="/recomendate", tags=["recomendate"])


@router.post('/')
async def recomendate(model: RecomendateModel, request: Request):
    user_data = Recomendate(
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
        study_form=model.study_form
    )
    recomendate = await send_data(model)
    return recomendate["data"]
    
    