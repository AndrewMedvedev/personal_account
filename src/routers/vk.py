from fastapi import APIRouter, Request, Response, status
from fastapi.responses import JSONResponse

from ..constants import PATH_ENDPOINT
from ..controllers import VKControl

vk = APIRouter(prefix=f"{PATH_ENDPOINT}vk", tags=["vk"])


@vk.get("/link")
async def vk_link() -> JSONResponse:
    return JSONResponse(status_code=status.HTTP_200_OK, content=await VKControl().link())


@vk.get("/get/token/{code}/{device_id}/{code_verifier}")
async def vk_get_token(code: str, device_id: str, code_verifier: str) -> JSONResponse:
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=await VKControl().get_token(
            code=code, device_id=device_id, code_verifier=code_verifier
        ),
    )


@vk.post("/registration/{access}")
async def vk_registration(access: str, request: Request) -> Response:
    await VKControl().registration(user_id=request.state.user_id, access=access)
    return Response(status_code=status.HTTP_201_CREATED)
