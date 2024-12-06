from fastapi import FastAPI
from src.routers.user_data import router as router_user_data
from src.routers.middleware import router as router_middleware
from src.routers.recomendate import router as router_recomendate

app = FastAPI(title="Личный Кабинет")
app.include_router(router_recomendate)
app.include_router(router_user_data)
app.include_router(router_middleware)
