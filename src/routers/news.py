from fastapi import APIRouter, status
from fastapi.responses import JSONResponse

from ..constants import PATH_ENDPOINT
from ..controllers import NewsControl

news = APIRouter(prefix=f"{PATH_ENDPOINT}news", tags=["news"])


@news.get("/get")
async def get(page: int = 1, limit: int = 10) -> JSONResponse:
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=await NewsControl().get_news(page=page, limit=limit),
    )
