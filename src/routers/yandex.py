from fastapi import APIRouter, Request, status
from fastapi.responses import JSONResponse

from src.classes.yandex_class import Yandex

router_yandex = APIRouter(prefix="/api/v1/yandex", tags=["yandex"])


@router_yandex.get(
    "/link",
    response_model=None,
)
async def yandex_link() -> JSONResponse:
    try:
        return await Yandex().link()
    except Exception as e:
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST, content={"detail": str(e)}
        )


@router_yandex.get(
    "/get/token/{code}/{code_verifier}",
    response_model=None,
)
async def yandex_get_token(code: str, code_verifier: str) -> JSONResponse:
    try:
        return await Yandex(code=code).get_token(code_verifier=code_verifier)
    except Exception as e:
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST, content={"detail": str(e)}
        )


@router_yandex.post(
    "/registration/{access}",
    response_model=None,
)
async def yandex_registration(
    access: str,
    request: Request,
) -> JSONResponse:
    try:
        access_token = request.cookies.get("access")
        refresh_token = request.cookies.get("refresh")
        return await Yandex(
            token_access=access_token,
            token_refresh=refresh_token,
            access=access,
        ).registration()
    except Exception as e:
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST, content={"detail": str(e)}
        )
