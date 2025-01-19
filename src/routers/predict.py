from fastapi import APIRouter, Request, HTTPException, status
from src.database.schemas import PredictModel, PredictFree
from src.classes.send_data_class import SendData


router = APIRouter(prefix="/predict", tags=["predict"])


@router.post("/")
async def predict(model: PredictModel, request: Request):
    tkn = request.cookies.get("access")
    data = await token(tkn)
    if data != None:
        recomendate = await SendData.send_data_recomendate(model)
        classifier = await SendData.send_data_classifier_applicants(
            model, directions=recomendate.get("data")
        )
        return {
            "recomendate": recomendate.get("data"),
            "classifier": classifier.get("predictions"),
        }
    else:
        return HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)


@router.post("/free")
async def predict_free(model: PredictFree):
    try:
        classifier = await SendData.send_data_classifier_applicant(model)
        return classifier.get("data")
    except:
        return HTTPException(status_code=status.HTTP_400_BAD_REQUEST)
