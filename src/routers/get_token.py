from fastapi import (
    APIRouter,
    Request,
    HTTPException,
    Response,
    status,
)



router = APIRouter(prefix="/get_token", tags=["get_token"])



@router.get("/")
async def get_token(access: str, refresh: str, response: Response):
    response.set_cookie(key="access", value=access, samesite="none", httponly=True, secure=True)
    response.set_cookie(key="refresh", value=refresh,  samesite="none", httponly=True, secure=True)
    return HTTPException(status_code=status.HTTP_200_OK)


