from typing import Literal

from uuid import UUID

from pydantic import BaseModel, field_validator

from config import settings

from .constants import MAX_BONUS_POINTS, MAX_EXAMS_POINTS, MAX_GPA, MIN_GPA


class PredictSchema(BaseModel):
    gender: Literal["male", "female"]
    gpa: float
    points: int
    bonus_points: int
    exams: list[dict]
    year: int

    @field_validator("gpa")
    @classmethod
    def validate_gpa(cls, v: float) -> float:
        if v < MIN_GPA or v > MAX_GPA:
            raise ValueError("Field gpa must be in range [3;5]")
        return v

    @field_validator("points")
    @classmethod
    def validate_exams_points(cls, v: int) -> int:
        if v < 0 or v > MAX_EXAMS_POINTS:
            raise ValueError("Field exams_points must be in range [0;310]")
        return v

    @field_validator("bonus_points")
    @classmethod
    def validate_bonus_points(cls, v: int) -> int:
        if v < 0 or v > MAX_BONUS_POINTS:
            raise ValueError("Field bonus_points must be in range [0;10]")
        return v

    def to_dict_get_data_recomendate(self) -> dict:
        return {
            "gender": self.gender,
            "gpa": self.gpa,
            "points": self.points,
            "exams": self.exams,
        }

    def to_dict_get_data_classifier_applicants(self, direction: str) -> dict:
        return {
            "year": self.year,
            "gender": self.gender,
            "gpa": self.gpa,
            "points": self.points,
            "direction": direction,
        }


class PredictFreeSchema(BaseModel):
    year: int
    gender: Literal["male", "female"]
    gpa: float
    points: int
    direction: str

    @field_validator("gpa")
    @classmethod
    def validate_gpa(cls, v: float) -> float:
        if v < MIN_GPA or v > MAX_GPA:
            raise ValueError("Field gpa must be in range [3;5]")
        return v

    @field_validator("points")
    @classmethod
    def validate_exams_points(cls, v: int) -> int:
        if v < 0 or v > MAX_EXAMS_POINTS:
            raise ValueError("Field exams_points must be in range [0;310]")
        return v

    def to_dict(self) -> dict:
        return {
            "year": self.year,
            "gender": self.gender,
            "gpa": self.gpa,
            "points": self.points,
            "direction": self.direction,
        }


class RegistrationVKSchema(BaseModel):
    user_id: UUID
    first_name: str
    last_name: str
    id_vk: int
    email: str

    @field_validator("user_id")
    @classmethod
    def valid_user_id(cls, v: UUID) -> str:
        return str(v)


class Codes(BaseModel):
    state: str
    code_verifier: str
    code_challenge: str


class RegistrationYandexSchema(BaseModel):
    user_id: UUID
    first_name: str
    last_name: str
    id_yandex: str
    login: str
    email: str

    @field_validator("user_id")
    @classmethod
    def valid_user_id(cls, v: UUID) -> str:
        return str(v)


class DictLinkVKSchema(BaseModel):
    response_type: Literal["code"] = "code"
    client_id: int = settings.VK_APP_ID
    scope: Literal["email"] = "email"
    redirect_uri: str = settings.VK_REDIRECT_URI
    state: str = settings.STATE_VK
    code_challenge: str
    code_challenge_method: str = "s256"


class DictGetDataVKSchema(BaseModel):
    grant_type: Literal["authorization_code"] = "authorization_code"
    code: str
    code_verifier: str
    client_id: int = settings.VK_APP_ID
    device_id: str
    redirect_uri: str = settings.VK_REDIRECT_URI
    state: str = settings.STATE_VK


class DictGetDataTokenVKSchema(BaseModel):
    access_token: str
    client_id: int = settings.VK_APP_ID


class DictLinkYandexSchema(BaseModel):
    response_type: Literal["code"] = "code"
    client_id: str = settings.YANDEX_APP_ID
    state: str
    code_challenge: str
    code_challenge_method: str = "S256"


class DictGetDataYandexSchema(BaseModel):
    grant_type: Literal["authorization_code"] = "authorization_code"
    code: str
    client_id: str = settings.YANDEX_APP_ID
    client_secret: str = settings.YANDEX_APP_SECRET
    code_verifier: str


class DictGetDataTokenYandexSchema(BaseModel):
    oauth_token: str
    format: Literal["json"] = "json"


class BaseMessage(BaseModel):
    chat_id: str
    role: Literal["user", "assistant"]
    text: str


class UserMessage(BaseMessage):
    role: Literal["user", "assistant"] = "user"


class AssistantMessage(BaseMessage):
    role: Literal["user", "assistant"] = "assistant"
