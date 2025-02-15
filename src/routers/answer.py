from fastapi import (
    APIRouter,
    Request,
    HTTPException,
    Response,
    status,
)
from fastapi.responses import JSONResponse
from src.classes import Answer

router_answer = APIRouter(prefix="/answer", tags=["answer"])


@router_answer.get(
    "/",
    response_model=None,
)
async def answer(
    message: str,
    request: Request,
    response: Response,
) -> dict | HTTPException:
    try:
        access = request.cookies.get("access")
        refresh = request.cookies.get("refresh")
        return await Answer(
            message=message,
            token_access=access,
            token_refresh=refresh,
            response=response,
        ).answer()
    except Exception as e:
        return JSONResponse(
            status_code=status.HTTP_401_UNAUTHORIZED,
            content={"detail": str(e)},
        )
