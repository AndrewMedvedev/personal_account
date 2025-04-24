from fastapi import APIRouter, Request, Response, status
from fastapi.responses import JSONResponse, StreamingResponse

from ..constants import PATH_ENDPOINT
from ..controllers import VisitorControl

visitors = APIRouter(prefix=f"{PATH_ENDPOINT}visitors", tags=["visitors"])


@visitors.post("/add/{event_id}")
async def add(event_id: int, request: Request) -> Response:
    await VisitorControl().create_user(user_id=request.state.user_id, event_id=event_id)
    return Response(status_code=status.HTTP_201_CREATED)


@visitors.get("/get")
async def get(request: Request) -> JSONResponse:
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=await VisitorControl().get_user_events(user_id=request.state.user_id),
    )


@visitors.get("/make/qr/{unique_string}")
async def make_qr(unique_string: str) -> StreamingResponse:
    return await VisitorControl().make_qr(unique_string=unique_string)


@visitors.delete("/delete/{event_id}")
async def delete(event_id: int, request: Request) -> Response:
    await VisitorControl().delete_user(user_id=request.state.user_id, event_id=event_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
