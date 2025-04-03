from fastapi import APIRouter, Request

from src.classes import News
from src.responses import CustomResponse

router_news = APIRouter(prefix="/api/v1/news", tags=["news"])


@router_news.get("/get")
async def get(
    request: Request,
    page: int = 1,
    limit: int = 10,
) -> CustomResponse:
    return await News().get_news(
        page=page,
        limit=limit,
    )
