from src.database.database import Base, int_pk, int_null, list_null, str_null, str_uniq
from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.postgresql import ARRAY



class PersonalData(Base):
    id: Mapped[int] = mapped_column(primary_key=True, unique=True)
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
    recomendate_id: Mapped[int] = mapped_column(
        ForeignKey("personaldatas.id", ondelete="CASCADE"),
        unique=True,
        primary_key=True,
    )
    top_n: Mapped[int_null]
    age: Mapped[int_null]
    gender: Mapped[str_null]
    sport: Mapped[str | None]
    foreign: Mapped[str_null]
    gpa: Mapped[int_null]
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
