from fastapi import APIRouter, Request, status
from fastapi.responses import JSONResponse

from src.classes.vk_class import VK

router_vk = APIRouter(prefix="/api/v1/vk", tags=["vk"])


@router_vk.get(
    "/link",
    response_model=None,
)
async def vk_link() -> JSONResponse:
    try:
        return await VK().link()
    except Exception as e:
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST, content={"detail": str(e)}
        )


@router_vk.get(
    "/get/token/{code}/{device_id}/{code_verifier}",
    response_model=None,
)
async def vk_get_token(
    code: str,
    device_id: str,
    code_verifier: str,
) -> JSONResponse:
    try:
        return await VK(
            code=code,
            device_id=device_id,
        ).get_token(code_verifier=code_verifier)
    except Exception as e:
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST, content={"detail": str(e)}
        )


@router_vk.post(
    "/registration/{access}",
    response_model=None,
)
async def vk_registration(
    access: str,
    request: Request,
) -> JSONResponse:
    try:
        access_token = request.cookies.get("access")
        refresh_token = request.cookies.get("refresh")
        return await VK(
            token_access=access_token,
            token_refresh=refresh_token,
            access=access,
        ).registration()
    except Exception as e:
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST, content={"detail": str(e)}
        )
