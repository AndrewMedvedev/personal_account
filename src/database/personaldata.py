from typing import TYPE_CHECKING
from src.database.database import Base, str_null, str_uniq
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.dialects.postgresql import ARRAY

if TYPE_CHECKING:
    from database.models import Recomendate, Classifier


class PersonalData(Base):
    id: Mapped[int] = mapped_column(primary_key=True)
    recomendate: Mapped[list["Recomendate"]] = relationship(
        back_populates="personaldatas"
    )
    classifier: Mapped[list["Classifier"]] = relationship(
        back_populates="personaldatas"
    )
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
