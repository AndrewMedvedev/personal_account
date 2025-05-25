from fastapi import APIRouter, Request, Response, status
from fastapi.responses import JSONResponse

from ..constants import PATH_ENDPOINT
from ..controllers import VKControl

vk = APIRouter(prefix=f"{PATH_ENDPOINT}vk", tags=["vk"])


@vk.get("/link")
async def vk_link() -> JSONResponse:
    return JSONResponse(status_code=status.HTTP_200_OK, content=await VKControl().link())


@vk.post("/registration/{code}/{device_id}/{state}")
async def vk_registration(request: Request, code: str, device_id: str, state: str) -> Response:
    await VKControl().registration(
        code=code, device_id=device_id, state=state, user_id=request.state.user_id
    )
    return Response(status_code=status.HTTP_201_CREATED)
