from fastapi import APIRouter, Response, Request, HTTPException, status
from src.classes.answer_class import Answer

router = APIRouter(prefix="/answer", tags=["answer"])


@router.get(
    "/",
    response_model=None,
)
async def answer(
    message: str,
    request: Request,
    response: Response,
) -> str | HTTPException:
    access = request.cookies.get("access")
    refresh = request.cookies.get("refresh")
    return await Answer(
        message=message,
        token_access=access,
        token_refresh=refresh,
        response=response,
    ).answer()
