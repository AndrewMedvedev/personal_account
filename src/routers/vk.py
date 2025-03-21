from fastapi import APIRouter, Request

from src.classes.vk_class import VK
from src.database.schemas import CustomResponse

router_vk = APIRouter(prefix="/api/v1/vk", tags=["vk"])


@router_vk.get(
    "/link",
    response_model=None,
)
async def vk_link() -> CustomResponse:
    return await VK().link()


@router_vk.get(
    "/get/token/{code}/{device_id}/{code_verifier}",
    response_model=None,
)
async def vk_get_token(
    code: str,
    device_id: str,
    code_verifier: str,
) -> CustomResponse:
    return await VK().get_token(
        code=code,
        device_id=device_id,
        code_verifier=code_verifier,
    )


@router_vk.post(
    "/registration/{access}",
    response_model=None,
)
async def vk_registration(
    access: str,
    request: Request,
) -> CustomResponse:
    return await VK().registration(
        user_id=request.state.user_id,
        access=access,
    )
