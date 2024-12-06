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


class Kostyl:
    def __init__(self, model):
        self.gender = model.gender
        self.age = model.age
        self.sport = model.sport
        self.foreign = model.foreign
        self.gpa = model.gpa
        self.total_points = model.total_points
        self.bonus_points = model.bonus_points
        self.exams = model.exams
        self.education = model.education
        self.study_form = model.study_form

    def get_params(self):
        return (
            self.gender,
            self.age,
            self.sport,
            self.foreign,
            self.gpa,
            self.total_points,
            self.bonus_points,
            self.exams,
            self.education,
            self.study_form,
        )
