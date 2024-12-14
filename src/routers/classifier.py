from fastapi import APIRouter, Request, HTTPException, status
from src.database.schemas import ClassifierModel
from src.database.models import Classifier
from src.database.services.crud import CRUD
from src.api.controls import send_data_classifier, token


router = APIRouter(prefix="/classifier", tags=["classifier"])


@router.post("/")
async def classifier(model: ClassifierModel, request: Request):
    tkn = request.cookies.get("access")
    data = await token(tkn)
    if data != None:
        user_data = Classifier(
            email=data,
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
        await CRUD().create_data(user_data)
        classifier = await send_data_classifier(model)

        return classifier
    else:
        return HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)