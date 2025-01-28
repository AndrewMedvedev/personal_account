from fastapi import (
    APIRouter,
    Request,
    HTTPException,
    status,
)
from fastapi.responses import JSONResponse
from src.classes.answer_class import Answer

router = APIRouter(prefix="/answer", tags=["answer"])


@router.get(
    "/",
    response_model=None,
)
async def answer(
    message: str,
    request: Request,
) -> dict | HTTPException:
    try:
        access = request.cookies.get("access")
        refresh = request.cookies.get("refresh")
        return await Answer(
            message=message,
            token_access=access,
            token_refresh=refresh,
        ).answer()
    except Exception as e:
        return JSONResponse(
            status_code=status.HTTP_401_UNAUTHORIZED,
            content={"detail": str(e)},
        )
