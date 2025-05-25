from typing import Any

import base64
import hashlib
import logging
import os
from uuid import uuid4

from fastapi import WebSocket
from redis.asyncio import Redis

from config import settings

from .exeptions import BadRequestHTTPError, ExistsHTTPError, NoPlacesHTTPError, NotFoundHTTPError
from .schemas import Codes


class RedisOtherAuth:
    def __init__(self):
        self.session = Redis(
            host=settings.REDIS_HOST,
            port=settings.REDIS_PORT,
            password=settings.REDIS_PASSWORD,
            decode_responses=True,
        )

    async def add_code(self, schema: Codes) -> None:
        await self.session.setex(name=schema.state, value=schema.code_verifier, time=120)

    async def get_code(self, key: str) -> str:
        result = await self.session.get(key)
        await self.session.delete(key)
        return result


class ConnectionManager:
    def __init__(self) -> None:
        self.connections: dict[str, WebSocket] = {}

    async def connect(self, websocket: WebSocket, chat_id: str) -> None:
        await websocket.accept()
        if chat_id not in self.connections:
            self.connections[chat_id] = websocket
        self.connections[chat_id]

    def disconnect(self, chat_id: str) -> None:
        if chat_id in self.connections:
            del self.connections[chat_id]

    async def send(self, message: str, chat_id: str) -> None:
        await self.connections[chat_id].send_text(message)


connection_manager = ConnectionManager()


def create_codes() -> Codes:
    code_verifier = base64.urlsafe_b64encode(os.urandom(64)).rstrip(b"=").decode("utf-8")
    code_challenge = (
        base64.urlsafe_b64encode(hashlib.sha256(code_verifier.encode("utf-8")).digest())
        .rstrip(b"=")
        .decode("utf-8")
    )
    return Codes(
        state=str(f"{uuid4()}{uuid4()}"),
        code_verifier=code_verifier,
        code_challenge=code_challenge,
    )


def config_logging(level=logging.INFO):
    logging.basicConfig(
        level=level,
        datefmt="%Y-%m-%d %H:%M:%S",
        format="[%(asctime)s] %(module)10s:%(lineno)-3d %(levelname)-7s - %(message)s",
    )


async def valid_answer(response: Any) -> None:
    status = response.status
    match status:
        case 200:
            return await response.json()
        case 201:
            return None
        case 204:
            return None
        case 400:
            raise BadRequestHTTPError
        case 403:
            raise NoPlacesHTTPError
        case 404:
            raise NotFoundHTTPError
        case 409:
            raise ExistsHTTPError
