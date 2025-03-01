from typing import Annotated

from sqlalchemy.orm import mapped_column

int_pk = Annotated[int, mapped_column(primary_key=True)]
int_null = Annotated[int, mapped_column(unique=True)]
int_null_true = Annotated[int, mapped_column(nullable=True)]
str_null_true = Annotated[str, mapped_column(nullable=True)]
str_null = Annotated[str, mapped_column(nullable=False)]
str_uniq = Annotated[str, mapped_column(unique=True)]
float_null = Annotated[float, mapped_column(nullable=False)]
