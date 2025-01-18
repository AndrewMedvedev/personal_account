import json
import aiohttp
from src.config import Settings


class SendData:

    def __init__(self, data) -> None:
        self.data = data

    async def send_data_recomendate(self) -> dict:
        async with aiohttp.ClientSession() as session:
            data = {
                "top_n": self.data.top_n,
                "user": {
                    "gender": self.data.gender,
                    "age": self.data.age,
                    "sport": self.data.sport,
                    "foreign": self.data.foreign,
                    "gpa": self.data.gpa,
                    "total_points": self.data.points,
                    "bonus_points": self.data.bonus_points,
                    "exams": self.data.exams,
                    "education": self.data.education,
                    "study_form": self.data.study_form,
                },
            }

            async with session.post(
                Settings.RECOMENDATE,
                json=data,
            ) as resp:
                rec = await resp.text()
                return json.loads(rec)

    async def send_data_classifier_applicants(self, directions: list) -> dict:
        async with aiohttp.ClientSession() as session:
            correct_data = {"applicants": []}
            array = [
                correct_data["applicants"].append(
                    {
                        "gender": self.data.gender,
                        "gpa": self.data.gpa,
                        "priority": self.data.priority,
                        "points": self.data.points,
                        "direction": i[23::],
                    }
                )
                for i in directions
            ]

            async with session.post(
                Settings.CLASSIFIER,
                json=correct_data,
            ) as resp:
                rec = await resp.text()
                return json.loads(rec)

    async def send_data_classifier_applicant(self) -> dict:
        async with aiohttp.ClientSession() as session:
            data = {
                "gender": self.data.gender,
                "gpa": self.data.gpa,
                "priority": self.data.priority,
                "points": self.data.points,
                "direction": self.data.direction,
            }

            async with session.post(
                Settings.CLASSIFIER_FREE,
                json=data,
            ) as resp:
                rec = await resp.text()
                return json.loads(rec)

    async def send_refresh_token(self) -> dict | bool:
        async with aiohttp.ClientSession() as session:
            data = self.data
            async with session.post(
                Settings.VALIDATE_REFRESH,
                data=data,
            ) as resp:
                tkn = await resp.text()
                try:
                    tkn = await resp.text()
                    return json.loads(tkn)
                except:
                    return False

    async def send_access_token(self) -> str:
        async with aiohttp.ClientSession() as session:
            data = self.data
            async with session.post(
                Settings.VALIDATE_ACCESS,
                data=data,
            ) as resp:
                return await resp.text()
