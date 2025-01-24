from pydantic import (
    BaseModel,
    Field,
)


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
