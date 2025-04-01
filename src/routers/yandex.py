from fastapi import APIRouter, Request

from src.classes.yandex_class import Yandex
from src.responses import CustomResponse

router_yandex = APIRouter(prefix="/api/v1/yandex", tags=["yandex"])


@router_yandex.get(
    "/link",
    response_model=None,
)
async def yandex_link() -> CustomResponse:
    return await Yandex().link()


@router_yandex.get(
    "/get/token/{code}/{code_verifier}",
    response_model=None,
)
async def yandex_get_token(
    code: str,
    code_verifier: str,
) -> CustomResponse:
    return await Yandex().get_token(
        code_verifier=code_verifier,
        code=code,
    )


@router_yandex.post(
    "/registration/{access}",
    response_model=None,
)
async def yandex_registration(
    access: str,
    request: Request,
) -> CustomResponse:
    return await Yandex().registration(
        user_id=request.state.user_id,
        access=access,
    )
