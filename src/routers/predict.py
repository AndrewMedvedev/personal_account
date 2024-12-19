from fastapi import APIRouter, Request, HTTPException, status
from src.database.schemas import PredictModel
from src.api.controls import send_data_recomendate, send_data_classifier, token


router = APIRouter(prefix="/predict", tags=["predict"])


@router.post("/")
async def predict(model: PredictModel, request: Request):
    tkn = request.cookies.get("access")
    data = await token(tkn)
    if data != None:
        recomendate = await send_data_recomendate(model)
        classifier = await send_data_classifier(model, speciality=recomendate["data"])
        return {"recomendate": recomendate["data"], "classifier": classifier["data"]}
    else:
        return HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
