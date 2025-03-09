from typing import Literal

from pydantic import BaseModel, field_validator


class PredictModel(BaseModel):
    gender: Literal["male", "female"]
    foreign_citizenship: str
    military_service: Literal["yes", "no"]
    gpa: float
    points: int
    bonus_points: int
    exams: list[dict]
    year: int

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
    gender: Literal["male", "female"]
    gpa: float
    points: int
    direction: str

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
