from fastapi import (
    APIRouter,
    HTTPException,
    status,
)
from src.classes.answer_class import Answer

router = APIRouter(prefix="/answer", tags=["answer"])


@router.get(
    "/",
    response_model=None,
)
async def answer(
    message: str,
    access: str,
    refresh: str,
) -> dict | HTTPException:
    try:
        return await Answer(
            message=message,
            token_access=access,
            token_refresh=refresh,
        ).answer()
    except:
        return HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
