import logging

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.errors import RateLimitExceeded
from slowapi.middleware import SlowAPIMiddleware
from slowapi.util import get_remote_address

from src.classes.controls import config_logging
from src.errors import (NotFoundError, SendError, TokenError, not_found_error,
                        send_error, token_error)
from src.middleware import MiddlewareValidTokens
from src.routers import (router_answer, router_logout, router_predict,
                         router_set_token, router_visitors, router_vk,
                         router_yandex)

limiter = Limiter(key_func=get_remote_address, default_limits=["10/second"])

config_logging(level=logging.INFO)

app = FastAPI(title="Личный Кабинет")

app.include_router(router_set_token)

app.include_router(router_logout)

app.include_router(router_vk)

app.include_router(router_yandex)

app.include_router(router_predict)

app.include_router(router_visitors)

app.include_router(router_answer)

app.state.limiter = limiter

app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

app.add_exception_handler(SendError, send_error)

app.add_exception_handler(TokenError, token_error)

app.add_exception_handler(NotFoundError, not_found_error)

app.add_middleware(MiddlewareValidTokens)

app.add_middleware(SlowAPIMiddleware)

origins = [
    "http://localhost:3000",
    "https://register-666-ramzer.onrender.com",
    "https://frontend-project-production-6352.up.railway.app",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"],
)
