from fastapi import (
    APIRouter,
    Request,
    HTTPException,
    Response,
    status,
)
from fastapi.responses import JSONResponse
from src.database.schemas.predict_schemas import (
    PredictModel,
    PredictFree,
)
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
    try:
        access = request.cookies.get("access")
        refresh = request.cookies.get("refresh")
        return await Predict(
            token_access=access,
            token_refresh=refresh,
            model=model,
            response=response,
        ).predict()
    except Exception as e:
        return JSONResponse(
            status_code=status.HTTP_401_UNAUTHORIZED, content={"detail": str(e)}
        )


@router.post(
    "/free",
    response_model=None,
)
async def predict_free(model: PredictFree) -> str | HTTPException:
    try:
        classifier = await SendData.send_data_classifier_applicant(model)
        return classifier.get("data")
    except Exception as e:
        return JSONResponse(
            status_code=status.HTTP_401_UNAUTHORIZED,
            content={"detail": str(e)},
        )
