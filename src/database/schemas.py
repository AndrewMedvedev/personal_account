from pydantic import BaseModel, Field, field_validator
from fastapi import HTTPException, status


class PersonalDataModel(BaseModel):
    first_name: str = Field(gt=1, lt=50)
    last_name: str = Field(gt=1, lt=50)
    dad_name: str = Field(gt=1, lt=50)
    bio: str = Field(lt=5000)
    school: str = Field(lt=100)


class RecomendateModel(BaseModel):
    top_n: str = Field(gt=1, lt=10)
    age: int = Field(gt=16)
    gender: str = Field(gt=1, lt=3)
    sport: str
    foreign: str
    gpa: int = Field(gt=3, le=5)
    total_points: int = Field(gt=130)
    bonus_points: int = Field(gt=1, le=10)
    exams: list
    education: str
    study_form: str
