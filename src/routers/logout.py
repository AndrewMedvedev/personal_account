from fastapi import APIRouter, Response

logout = APIRouter(prefix="/logout", tags=["logout"])


@logout.get("/")
async def logout_(response: Response) -> Response:
    response.delete_cookie(
        key="access",
        samesite=None,
        httponly=False,
        secure=True,
    )
    response.delete_cookie(
        key="refresh",
        samesite=None,
        httponly=False,
        secure=True,
    )
    return {"message": "success"}
