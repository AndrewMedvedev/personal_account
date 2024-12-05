from pydantic import BaseModel, Field, field_validator
from fastapi import HTTPException, status


class UserModel(BaseModel):
    first_name: str = Field(ge=2, le=20)
    last_name: str = Field(ge=2, le=30)
    dad_name: str = Field(ge=2, le=30)
    hobby: str = Field(le=100)
    gender: str = Field(ge=1, le=1)
    hostel: str = Field(gt=1, le=4)
    gpa: int = Field(gt=100)
    priority: int
    exams_points: int
    bonus_points: int
    education: str
    study_form: str
    reception_form: str
    speciality: str
