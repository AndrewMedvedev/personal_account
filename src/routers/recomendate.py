from src.database.services.crud import CRUD
from src.database.models import Recomendate
from src.database.schema_rec import RecomendateData, Kostyl
from fastapi import APIRouter
import asyncio
import aiohttp


router = APIRouter(prefix="/recomendate", tags="recomendate")


async def send_data(email):
    async with aiohttp.ClientSession() as session:
        stmt = await CRUD().read_data(model=Recomendate, email=email)
        data = RecomendateData(
            top_n=stmt.top_n,
            user=Kostyl(stmt).get_params()
        )
        async with session.post(
            "https://tyuiu-fastapi-rec-sys.onrender.com/rec_sys/recommend/", json=data
        ) as resp:
            return await resp.text()


print(asyncio.run(send_data()))
