from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.routers.user_data import router as router_user_data
from src.routers.predict import router as router_predict
from src.routers.logout import router as router_logout
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.middleware import SlowAPIMiddleware
from slowapi.errors import RateLimitExceeded

limiter = Limiter(key_func=get_remote_address, default_limits=["10/second"])

app = FastAPI(title="Личный Кабинет")

app.include_router(router_user_data)

app.include_router(router_logout)

app.include_router(router_predict)

app.state.limiter = limiter

app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

app.add_middleware(SlowAPIMiddleware)

origins = ["http://localhost:3000"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"],
)
