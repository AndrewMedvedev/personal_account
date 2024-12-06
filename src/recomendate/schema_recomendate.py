from typing import List, Literal
from pydantic import BaseModel, ConfigDict


class RecomendateDataModel(BaseModel):
    gender: Literal["М", "Ж"]
    age: int
    sport: str
    foreign: str
    gpa: float
    total_points: int
    bonus_points: int
    exams: List[str]
    education: str
    study_form: str


class RecomendateData(BaseModel):
    top_n: int
    user: RecomendateDataModel

    model_config = ConfigDict(from_attributes=True)
