import typing

from pydantic import BaseModel


class CustomResponse(BaseModel):
    status_code: int
    body: typing.Any
    message: str
    name_endpoint: str
