from typing import List
from pydantic import BaseModel, Field, field_validator


class PersonalDataModel(BaseModel):
    first_name: str
    last_name: str
    dad_name: str
    bio: str


class PersonalDataModelUpdate(PersonalDataModel):
    first_name: str | None = Field(default=None)
    last_name: str | None = Field(default=None)
    dad_name: str | None = Field(default=None)
    bio: str | None = Field(default=None)


class RecomendateModel(BaseModel):
    top_n: str
    age: int = Field(gt=16)
    gender: str
    sport: str
    foreign: str
    gpa: float = Field(gt=3, le=5)
    total_points: int = Field(gt=130)
    bonus_points: int = Field(gt=1, le=10)
    exams: List[str]
    education: str
    study_form: str


class ClassifierModel(BaseModel):
    gender: str
    hostel: str
    gpa: float = Field(gt=3, le=5)
    priority: int
    exams_points: int
    bonus_points: int = Field(gt=1, le=10)
    education: str
    study_form: str
    reception_form: str
    speciality: str
