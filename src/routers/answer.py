from fastapi import APIRouter, Request

from src.classes import Answer
from src.database.schemas import CustomResponse

router_answer = APIRouter(prefix="/api/v1/answer", tags=["answer"])


@router_answer.get(
    "/{message}",
    response_model=None,
)
async def answer(
    message: str,
    request: Request,
) -> CustomResponse:
    token_access = request.cookies.get("access")
    token_refresh = request.cookies.get("refresh")
    return await Answer().get_answer(
        message=message,
        token_access=token_access,
        token_refresh=token_refresh,
    )
