from fastapi import APIRouter, Request
from src.database.schemas import ClassifierModel
from src.database.models import Classifier
from src.api.controls import send_data_classifier


router = APIRouter(prefix="/classifier", tags=["classifier"])


@router.post("/")
async def classifier(model: ClassifierModel):
    user_data = Classifier(
        gender=model.gender,
        hostel=model.hostel,
        gpa=model.gpa,
        priority=model.priority,
        exams_points=model.exams_points,
        bonus_points=model.bonus_points,
        education=model.education,
        study_form=model.study_form,
        reception_form=model.reception_form,
        speciality=model.speciality,
    )
    classifier = await send_data_classifier(model)

    return classifier["data"]
