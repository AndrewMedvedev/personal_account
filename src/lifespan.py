from typing import Any

from contextlib import asynccontextmanager

from fastapi import FastAPI
from faststream.rabbit import RabbitBroker

from config import get_rabbit_url

broker = RabbitBroker(url=get_rabbit_url())


@asynccontextmanager
async def lifespan(app: FastAPI) -> Any:  # noqa: ARG001
    await broker.connect()
    yield
    await broker.close()
