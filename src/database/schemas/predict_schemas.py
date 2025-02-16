from typing import List, Literal

from pydantic import BaseModel, field_validator


class PredictModel(BaseModel):
    top_n: str
    age: int
    year: int
    gender: Literal["М", "Ж"]
    sport: str
    foreign: str
    gpa: float
    points: int
    bonus_points: int
    exams: List[str]
    reception_form: str
    education: str
    study_form: Literal["Очная", "Заочная", "Очно-Заочная"]

    @field_validator("top_n")
    @classmethod
    def validate_top_n(cls, v: str) -> float:
        if int(v) <= 5 or int(v) > 1:
            raise ValueError("Field top_n, incorrect number of directions")
        return v

    @field_validator("age")
    @classmethod
    def validate_age(cls, v: int) -> int:
        if v < 16:
            raise ValueError("Field age must be over 16")
        return v

    @field_validator("year")
    @classmethod
    def validate_year(cls, v: int) -> float:
        if v < 2100 or v > 2023:
            raise ValueError("Field year ,wrong year")
        return v

    @field_validator("gpa")
    @classmethod
    def validate_gpa(cls, v: float) -> float:
        if v < 3 or v > 5:
            raise ValueError("Field gpa must be in range [3;5]")
        return v

    @field_validator("points")
    @classmethod
    def validate_exams_points(cls, v: int) -> int:
        if v < 0 or v > 310:
            raise ValueError("Field exams_points must be in range [0;310]")
        return v

    @field_validator("bonus_points")
    @classmethod
    def validate_bonus_points(cls, v: int) -> int:
        if v < 0 or v > 10:
            raise ValueError("Field bonus_points must be in range [0;10]")
        return v


class PredictFree(BaseModel):
    year: int
    gender: Literal["М", "Ж"]
    gpa: float
    points: int
    direction: str

    @field_validator("year")
    @classmethod
    def validate_year(cls, v: int) -> float:
        if v < 2100 or v > 2023:
            raise ValueError("Field year ,wrong year")
        return v

    @field_validator("gpa")
    @classmethod
    def validate_gpa(cls, v: float) -> float:
        if v < 3 or v > 5:
            raise ValueError("Field gpa must be in range [3;5]")
        return v

    @field_validator("points")
    @classmethod
    def validate_exams_points(cls, v: int) -> int:
        if v < 0 or v > 310:
            raise ValueError("Field exams_points must be in range [0;310]")
        return v
