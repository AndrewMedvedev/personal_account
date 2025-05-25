from fastapi import APIRouter, Request, Response, status
from fastapi.responses import JSONResponse

from ..constants import PATH_ENDPOINT
from ..controllers import YandexControl

yandex = APIRouter(prefix=f"{PATH_ENDPOINT}yandex", tags=["yandex"])


@yandex.get("/link")
async def yandex_link() -> JSONResponse:
    return JSONResponse(status_code=status.HTTP_200_OK, content=await YandexControl().link())


@yandex.post("/registration/{code}/{state}")
async def yandex_registration(code: str, state: str, request: Request) -> Response:
    await YandexControl().registration(
        user_id=request.state.user_id,
        code=code,
        state=state,
    )
    return Response(status_code=status.HTTP_201_CREATED)
