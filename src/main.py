from fastapi import FastAPI
from routers.recomendate import router as router_recomendate
from routers.user_data import router as router_user_data


app = FastAPI("Личный Кабинет")
app.include_router(router_recomendate)
app.include_router(router_user_data)
