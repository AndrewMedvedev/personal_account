from fastapi import APIRouter, Request, Response

from src.classes import Predict
from src.database.schemas import CustomResponse, PredictFree, PredictModel

router_predict = APIRouter(prefix="/api/v1/predict", tags=["predict"])


@router_predict.post(
    "/",
    response_model=None,
)
async def predict(
    model: PredictModel,
    request: Request,
) -> CustomResponse:
    token_access = request.cookies.get("access")
    token_refresh = request.cookies.get("refresh")
    return await Predict().predict(
        model=model,
        token_access=token_access,
        token_refresh=token_refresh,
    )


@router_predict.get(
    "/direction/{direction_id}",
    response_model=None,
)
async def direction(
    direction_id: int,
    request: Request,
) -> CustomResponse:
    token_access = request.cookies.get("access")
    token_refresh = request.cookies.get("refresh")
    return await Predict().get_direction(
        direction_id=direction_id,
        token_access=token_access,
        token_refresh=token_refresh,
    )


@router_predict.get(
    "/points/{direction_id}",
    response_model=None,
)
async def points(
    direction_id: int,
    request: Request,
) -> CustomResponse:
    token_access = request.cookies.get("access")
    token_refresh = request.cookies.get("refresh")
    return await Predict().get_points(
        direction_id=direction_id,
        token_access=token_access,
        token_refresh=token_refresh,
    )


@router_predict.post(
    "/free",
    response_model=None,
)
async def predict_free(
    model: PredictFree,
    response: Response,
) -> CustomResponse:
    return await Predict().predict_free(model=model)
