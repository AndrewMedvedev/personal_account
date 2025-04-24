from fastapi import APIRouter, status
from fastapi.responses import JSONResponse

from ..constants import PATH_ENDPOINT
from ..controllers import PredictControl
from ..schemas import PredictFreeSchema, PredictSchema

predicts = APIRouter(prefix=f"{PATH_ENDPOINT}predict", tags=["predict"])


@predicts.post("/")
async def predict(model: PredictSchema) -> JSONResponse:
    return JSONResponse(
        status_code=status.HTTP_200_OK, content=await PredictControl().predict(model=model)
    )


@predicts.post("/free")
async def predict_free(model: PredictFreeSchema) -> JSONResponse:
    return JSONResponse(
        status_code=status.HTTP_200_OK, content=await PredictControl().predict_free(model=model)
    )


@predicts.get("/direction/{direction_id}")
async def direction(direction_id: int) -> JSONResponse:
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=await PredictControl().get_direction(direction_id=direction_id),
    )


@predicts.get("/points/{direction_id}")
async def points(direction_id: int) -> JSONResponse:
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=await PredictControl().get_points(direction_id=direction_id),
    )


@predicts.get("/exams/{direction_id}")
async def exams(direction_id: int) -> JSONResponse:
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=await PredictControl().get_exams(direction_id=direction_id),
    )
