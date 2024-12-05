from sqlalchemy.orm import Mapped, mapped_column
from src.database.database import Base, int_pk, int_null, str_null, str_uniq
from sqlalchemy import ForeignKey


class PersonalData(Base):
    id: Mapped[int_pk]
    first_name: Mapped[str_null]
    last_name: Mapped[str_null]
    dad_name: Mapped[str | None]
    hobby: Mapped[str | None]
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
    recomendate_id: Mapped[int | None] = mapped_column(
        ForeignKey("personaldatas.id"),
        primary_key=True,
    )
    gender: Mapped[str_null]
    hostel: Mapped[str | None]
    gpa: Mapped[int_null]
    priority: Mapped[int_null]
    exams_points: Mapped[int_null]
    bonus_points: Mapped[int | None]
    education: Mapped[str_null]
    study_form: Mapped[str | None]
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
