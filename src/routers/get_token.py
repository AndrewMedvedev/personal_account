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
    response.set_cookie(key="access", value=access)
    response.set_cookie(key="refresh", value=refresh)
    return HTTPException(status_code=status.HTTP_200_OK)


