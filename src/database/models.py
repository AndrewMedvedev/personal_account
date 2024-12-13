from src.database.database import Base, float_null, int_null, str_null, str_uniq
from sqlalchemy import Column, ForeignKey, String, Table
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.postgresql import ARRAY


class PersonalData(Base):
    id: Mapped[int] = mapped_column(primary_key=True, unique=True)
    email: Mapped[str_uniq]
    first_name: Mapped[str_null]
    last_name: Mapped[str_null]
    dad_name: Mapped[str | None]
    bio: Mapped[str | None]
    school: Mapped[str | None]

    def __str__(self):
        return (
            f"{self.__class__.__name__}(id={self.id}, "
            f"first_name={self.first_name!r},"
            f"last_name={self.last_name!r})"
        )

    def __repr__(self):
        return str(self)


class Recomendate(Base):
    id: Mapped[int] = mapped_column(mapped_column(primary_key=True, unique=True))
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
    id: Mapped[int] = mapped_column(mapped_column(primary_key=True, unique=True))
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


class TableConnections(Base):
    personaldata_id = mapped_column(ForeignKey('personaldatas.id'),primary_key=True,ondelete="CASCADE")
    recomendate_id = mapped_column(ForeignKey('recomendates.id'),primary_key=True,ondelete="CASCADE")
    classifier_id = mapped_column(ForeignKey('classifiers.id'),primary_key=True,ondelete="CASCADE")