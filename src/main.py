from fastapi import FastAPI
from routers.user_data import router as router_user_data
from routers.middleware import router as router_middleware
from routers.recomendate import router as router_recomendate

app = FastAPI("Личный Кабинет")
app.include_router(router_recomendate)
app.include_router(router_user_data)
app.include_router(router_middleware)
