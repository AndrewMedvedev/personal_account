from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.errors import RateLimitExceeded
from slowapi.middleware import SlowAPIMiddleware
from slowapi.util import get_remote_address

from src.routers import (router_answer, router_get_token, router_logout,
                         router_predict)

limiter = Limiter(key_func=get_remote_address, default_limits=["10/second"])

app = FastAPI(title="Личный Кабинет")

app.include_router(router_answer)

app.include_router(router_get_token)

app.include_router(router_logout)

app.include_router(router_predict)

app.state.limiter = limiter

app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

app.add_middleware(SlowAPIMiddleware)

origins = [
    "http://localhost:3000",
    "https://register-666-ramzer.onrender.com",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=[
        "GET",
        "POST",
        "PUT",
        "OPTIONS",
    ],
    allow_headers=[
        "Content-Type",
        "Cookie",
    ],
    expose_headers=["*"],
)
