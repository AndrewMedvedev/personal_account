from typing import TYPE_CHECKING
from src.database.database import Base, float_null, int_null, str_null
from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.dialects.postgresql import ARRAY

if TYPE_CHECKING:
    from database.personaldata import PersonalData


class Recomendate(Base):
    id: Mapped[int] = mapped_column(primary_key=True)
    personaldata_id: Mapped[int] = mapped_column(
        ForeignKey("personaldatas.id"), nullable=False
    )
    personaldata: Mapped["PersonalData"] = relationship(back_populates="personaldatas")
    top_n: Mapped[str_null]
    age: Mapped[int_null]
    gender: Mapped[str_null]
    sport: Mapped[str | None]
    foreign: Mapped[str_null]
    gpa: Mapped[float_null]
    total_points: Mapped[int_null]
    bonus_points: Mapped[int_null]
    exams: Mapped[list[str]] = Column(ARRAY(String))
    education: Mapped[str_null]
    study_form: Mapped[str_null]

    def __str__(self):
        return (
            f"{self.__class__.__name__}(id={self.id}, "
            f"first_name={self.first_name!r},"
            f"last_name={self.last_name!r})"
        )

    def __repr__(self):
        return str(self)


class Classifier(Base):
    id: Mapped[int] = mapped_column(primary_key=True)
    personaldata_id: Mapped[int] = mapped_column(
        ForeignKey("personaldatas.id"), nullable=False
    )
    personaldata: Mapped["PersonalData"] = relationship(back_populates="personaldatas")
    gender: Mapped[str_null]
    hostel: Mapped[str_null]
    gpa: Mapped[float_null]
    priority: Mapped[int_null]
    exams_points: Mapped[int_null]
    bonus_points: Mapped[int_null]
    education: Mapped[str_null]
    study_form: Mapped[str_null]
    reception_form: Mapped[str_null]
    speciality: Mapped[str_null]

    def __str__(self):
        return (
            f"{self.__class__.__name__}(id={self.id}, "
            f"first_name={self.first_name!r},"
            f"last_name={self.last_name!r})"
        )

    def __repr__(self):
        return str(self)
