from fastapi import APIRouter, Request, HTTPException, status
from src.database.schemas import PredictModel, PredictFree
from src.api.controls import (
    send_data_recomendate,
    send_data_classifier_applicants,
    send_data_classifier_applicant,
    token,
)


router = APIRouter(prefix="/predict", tags=["predict"])


@router.post("/")
async def predict(model: PredictModel, request: Request):
    tkn = request.cookies.get("access")
    data = await token(tkn)
    # if data != None:
    recomendate = await send_data_recomendate(model)
    classifier = await send_data_classifier_applicants(
        model, direction=recomendate["data"]
    )
    return {
        "recomendate": recomendate["data"],
        "classifier": classifier["predictions"],
        }
    # else:
    #     return HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)


@router.post("/free")
async def predict_free(model: PredictFree):
    try:
        classifier = await send_data_classifier_applicant(model)
        return classifier["data"]
    except:
        return HTTPException(status_code=status.HTTP_400_BAD_REQUEST)
