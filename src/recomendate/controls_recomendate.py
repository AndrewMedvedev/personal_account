import json
from src.database.services.crud import CRUD
import asyncio
import aiohttp


async def send_data(data):
    async with aiohttp.ClientSession() as session:
        data = {
            "top_n": data.top_n,
            "user": {
                "gender": data.gender,
                "age": data.age,
                "sport": data.sport,
                "foreign": data.foreign,
                "gpa": data.gpa,
                "total_points": data.total_points,
                "bonus_points": data.bonus_points,
                "exams": data.exams,
                "education": data.education,
                "study_form": data.study_form,
            },
        }

        async with session.post(
            "https://tyuiu-fastapi-rec-sys.onrender.com/rec_sys/recommend/", json=data
        ) as resp:
            rec = await resp.text()
            return json.loads(rec)
