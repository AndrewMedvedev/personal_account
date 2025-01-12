from src.database.database import Base, str_null, int_null_true, int_null, str_null_true
from sqlalchemy.orm import Mapped, mapped_column


class PersonalData(Base):
    id: Mapped[int] = mapped_column(primary_key=True)
    id_vk: Mapped[int_null_true | None]
    phone_number: Mapped[str_null_true | None]
    email: Mapped[str_null_true | None]
    first_name: Mapped[str_null]
    last_name: Mapped[str_null]
    dad_name: Mapped[str | None]
    bio: Mapped[str | None]
    registration_type: Mapped[str]

    def __str__(self):
        return (
            f"{self.__class__.__name__}(id={self.id}, "
            f"first_name={self.first_name!r},"
            f"last_name={self.last_name!r})"
        )

    def __repr__(self):
        return str(self)
