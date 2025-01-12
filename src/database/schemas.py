from typing import List, Literal
from fastapi import HTTPException, status
import phonenumbers
from pydantic import BaseModel, Field, field_validator


class PersonalDataModel(BaseModel):
    phone_number: str
    first_name: str
    last_name: str
    dad_name: str
    bio: str

    @field_validator("phone_number")
    @classmethod
    def validate_phone_number(cls, values: str) -> str:
        parsed_number = phonenumbers.parse(values)
        if phonenumbers.is_valid_number(parsed_number):
            return values
        else:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Номер телефона должен начинаться с "
                + " и содержать от 1 до 15 цифр",
            )


class PersonalDataModelUpdate(PersonalDataModel):
    first_name: str | None = Field(default=None)
    last_name: str | None = Field(default=None)
    dad_name: str | None = Field(default=None)
    bio: str | None = Field(default=None)


class PredictModel(BaseModel):
    top_n: str
    age: int
    gender: Literal["М", "Ж"]
    sport: str
    foreign: str
    gpa: float
    points: int
    bonus_points: int
    exams: List[str]
    reception_form: str
    priority: int
    education: str
    study_form: Literal["Очная", "Заочная", "Очно-Заочная"]

    @field_validator("age")
    @classmethod
    def validate_age(cls, v: int) -> int:
        if v < 16:
            raise ValueError("Field age must be over 16")
        return v

    @field_validator("gpa")
    @classmethod
    def validate_gpa(cls, v: float) -> float:
        if v < 3 or v > 5:
            raise ValueError("Field gpa must be in range [3;5]")
        return v

    @field_validator("priority")
    @classmethod
    def validate_priority(cls, v: int) -> int:
        if v < 1 or v > 5:
            raise ValueError("Field priority must be in range [1;5]")
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
    gender: Literal["М", "Ж"]
    gpa: float
    priority: int
    points: int
    direction: str

    @field_validator("gpa")
    @classmethod
    def validate_gpa(cls, v: float) -> float:
        if v < 3 or v > 5:
            raise ValueError("Field gpa must be in range [3;5]")
        return v

    @field_validator("priority")
    @classmethod
    def validate_priority(cls, v: int) -> int:
        if v < 1 or v > 5:
            raise ValueError("Field priority must be in range [1;5]")
        return v

    @field_validator("points")
    @classmethod
    def validate_exams_points(cls, v: int) -> int:
        if v < 0 or v > 310:
            raise ValueError("Field exams_points must be in range [0;310]")
        return v
