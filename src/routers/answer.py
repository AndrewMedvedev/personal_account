from fastapi import APIRouter, status
from fastapi.responses import JSONResponse

from ..constants import PATH_ENDPOINT
from ..controllers import AnswerControl

answer = APIRouter(prefix=f"{PATH_ENDPOINT}answer", tags=["answer"])


@answer.get("/{message}")
async def answer_(message: str) -> JSONResponse:
    return JSONResponse(
        status_code=status.HTTP_200_OK, content=await AnswerControl().answer(message=message)
    )
