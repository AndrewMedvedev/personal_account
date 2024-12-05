from fastapi import APIRouter
import asyncio
import aiohttp


router = APIRouter(prefix="/recomendate", tags="recomendate")

data = {
    "top_n": 10,
    "user": {
        "gender": "М",
        "age": 19,
        "sport": "Футбол",
        "foreign": "Россия",
        "gpa": "4.3",
        "total_points": 220,
        "bonus_points": 10,
        "exams": ["Русский язык", "Математика", "Физика"],
        "education": "Среднее общее образование",
        "study_form": "Очная",
    },
}


async def send_data():
    async with aiohttp.ClientSession() as session:
        async with session.post(
            "https://tyuiu-fastapi-rec-sys.onrender.com/rec_sys/recommend/", json=data
        ) as resp:
            print(resp.status)
            print(await resp.text())


asyncio.run(send_data())
