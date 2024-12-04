from sqlalchemy.orm import Mapped
from src.database.database import (Base,
                                   str_null_true, 
                                   str_nullable, 
                                   int_pk ,
                                   int_null,
                                   int_null_true)


class User(Base):
    id: Mapped[int_pk]
    first_name: Mapped[str_nullable]
    last_name: Mapped[str_nullable]
    dad_name: Mapped[str_null_true] | None
    hobby: Mapped[str_null_true] | None 
    gender: Mapped[str_nullable]
    hostel: Mapped[str_null_true] | None
    gpa: Mapped[int_null] 
    priority: Mapped[int_null] 
    exams_points: Mapped[int_null] | 0
    bonus_points: Mapped[int_null_true] | 0
    education: Mapped[str_nullable]
    study_form: Mapped[str_null_true] | None 
    reception_form: Mapped[str_nullable]
    speciality: Mapped[str_nullable]

    
    def __str__(self):
        return (f"{self.__class__.__name__}(id={self.id}, "
            f"first_name={self.first_name!r},"
            f"last_name={self.last_name!r})")


    def __repr__(self):
        return str(self)

