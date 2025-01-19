from fastapi import APIRouter, HTTPException, status, Response

router = APIRouter(prefix="/logout", tags=["logout"])


@router.post(
    "/",
    response_model=None,
)
async def logout(response: Response) -> HTTPException:
    response.delete_cookie(key="access")
    response.delete_cookie(key="refresh")
    return HTTPException(status_code=status.HTTP_200_OK)
