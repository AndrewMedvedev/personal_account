from fastapi import APIRouter, Request, Response, status
from fastapi.responses import JSONResponse

from ..constants import PATH_ENDPOINT
from ..controllers import YandexControl

yandex = APIRouter(prefix=f"{PATH_ENDPOINT}yandex", tags=["yandex"])


@yandex.get("/link")
async def yandex_link() -> JSONResponse:
    return JSONResponse(status_code=status.HTTP_200_OK, content=await YandexControl().link())


@yandex.get("/get/token/{code}/{code_verifier}")
async def yandex_get_token(code: str, code_verifier: str) -> JSONResponse:
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=await YandexControl().get_token(code_verifier=code_verifier, code=code),
    )


@yandex.post("/registration/{access}")
async def yandex_registration(access: str, request: Request) -> Response:
    await YandexControl().registration(
        user_id=request.state.user_id,
        access=access,
    )
    return Response(status_code=status.HTTP_201_CREATED)
