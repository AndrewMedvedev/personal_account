from fastapi import APIRouter, Request

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
    return await Predict().predict(
        model=model,
    )


@router_predict.post(
    "/free",
    response_model=None,
)
async def predict_free(
    model: PredictFree,
) -> CustomResponse:
    return await Predict().predict_free(model=model)


@router_predict.get(
    "/direction/{direction_id}",
    response_model=None,
)
async def direction(
    direction_id: int,
    request: Request,
) -> CustomResponse:
    return await Predict().get_direction(
        direction_id=direction_id,
    )


@router_predict.get(
    "/points/{direction_id}",
    response_model=None,
)
async def points(
    direction_id: int,
    request: Request,
) -> CustomResponse:
    return await Predict().get_points(
        direction_id=direction_id,
    )


@router_predict.get(
    "/exams/{direction_id}",
    response_model=None,
)
async def exams(
    direction_id: int,
    request: Request,
) -> CustomResponse:
    return await Predict().get_exams(
        direction_id=direction_id,
    )
