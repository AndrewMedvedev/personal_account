from fastapi import HTTPException, status
from jose.exceptions import JWTError
from src.config import Settings as setting
from jose import jwt
import json
import aiohttp


async def send_data_recomendate(data):
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


async def send_data_classifier(data):
    async with aiohttp.ClientSession() as session:
        data = {
            "gender": data.gender,
            "hostel": data.hostel,
            "gpa": data.gpa,
            "priority": data.priority,
            "exams_points": data.exams_points,
            "bonus_points": data.bonus_points,
            "education": data.education,
            "study_form": data.study_form,
            "reception_form": data.reception_form,
            "speciality": data.speciality,
        }

        async with session.post(
            "https://tyuiu-fastapi-classifier.onrender.com/classifier/predict/",
            json=data,
        ) as resp:
            rec = await resp.text()
            return json.loads(rec)


async def token(token):
    if not token:
        return HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    else:
        try:
            access = jwt.decode(token, setting.SECRET_KEY, algorithms=setting.ALGORITHM)
            if "user_name" not in access and "mode" not in access:
                return HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
            if access["mode"] != "access_token":
                return HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
            return access["user_name"]
        except JWTError:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
            )
