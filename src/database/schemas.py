from pydantic import BaseModel, Field, field_validator
from fastapi import HTTPException, status


class PersonalDataModel(BaseModel):
    first_name: str = Field(gt=1, lt=50)
    last_name: str = Field(gt=1, lt=50)
    dad_name: str = Field(gt=1, lt=50)
    bio: str = Field(lt=5000)
    school: str = Field(lt=100)
    
    
class RecomendateModel(BaseModel):
    gender: str = Field(gt=1, lt=3)
    hostel: str = Field(gt=1, lt=50)
    gpa: int = Field(gt=3, le=5)
    priority: int
    exams_points: int = Field(gt=120)
    bonus_points: int
    edication: str = Field(gt=1, lt=50)
    study_form: str = Field(gt=1, lt=50)
    reception_form: str = Field(gt=1, lt=50)
    speciality: str = Field(gt=1, lt=100)