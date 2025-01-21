from fastapi import APIRouter, Request, HTTPException, Response, status
from src.database.schemas import PredictModel, PredictFree
from src.classes.send_data_class import SendData
from src.classes.predict_class import Predict


router = APIRouter(prefix="/predict", tags=["predict"])


@router.post(
    "/",
    response_model=None,
)
async def predict(
    model: PredictModel,
    request: Request,
    response: Response,
) -> dict | HTTPException:
    access = request.cookies.get("access")
    refresh = request.cookies.get("refresh")
    return await Predict(
        token_access=access,
        token_refresh=refresh,
        model=model,
        response=response,
    ).predict()


@router.post(
    "/free",
    response_model=None,
)
async def predict_free(model: PredictFree) -> str | HTTPException:
    try:
        classifier = await SendData.send_data_classifier_applicant(model)
        return classifier.get("data")
    except:
        return HTTPException(status_code=status.HTTP_400_BAD_REQUEST)
