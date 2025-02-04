from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.routers.get_token import router as router_get_token
from src.routers.logout import router as router_logout
from src.routers.predict import router as router_predict
from src.routers.answer import router as router_answer
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.middleware import SlowAPIMiddleware
from slowapi.errors import RateLimitExceeded

limiter = Limiter(key_func=get_remote_address, default_limits=["10/second"])

app = FastAPI(title="Личный Кабинет")

app.include_router(router_get_token)

app.include_router(router_logout)

app.include_router(router_predict)

app.include_router(router_answer)

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
    ],  # include additional methods as per the application demand
    allow_headers=[
        "Content-Type",
        "Cookie",
    ],
    expose_headers=["*"],
)
