from src.database.services.crud import CRUD
from src.database.models import Recomendate
from recomendate.schema_recomendate import RecomendateData
import asyncio
import aiohttp


async def send_data(email):
    async with aiohttp.ClientSession() as session:
        stmt = await CRUD().read_data(model=Recomendate, email=email)
        data = RecomendateData(
            top_n=stmt.top_n,
            user=(
                stmt.gender,
                stmt.age,
                stmt.sport,
                stmt.foreign,
                stmt.gpa,
                stmt.total_points,
                stmt.bonus_points,
                stmt.exams,
                stmt.education,
                stmt.study_form,
            ),
        )
        async with session.post(
            "https://tyuiu-fastapi-rec-sys.onrender.com/rec_sys/recommend/", json=data
        ) as resp:
            return await resp.text()


print(asyncio.run(send_data()))
