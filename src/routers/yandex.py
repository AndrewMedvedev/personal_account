from fastapi import APIRouter, Request

from src.classes.yandex_class import Yandex
from src.database.schemas import CustomResponse

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
    token_access = request.cookies.get("access")
    token_refresh = request.cookies.get("refresh")
    return await Yandex().registration(
        token_access=token_access,
        token_refresh=token_refresh,
        access=access,
    )
