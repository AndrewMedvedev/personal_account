from src.database.schemas.personal_data_schemas import PersonalDataModel
from src.database.services.orm import DatabaseSessionService
from sqlalchemy import Result, select
from src.database.models import PersonalData


class CRUD(DatabaseSessionService):
    def __init__(self) -> None:
        super().__init__()
        self.init()

    async def add_or_update_data_email(
        self,
        model,
        new_model,
        email: str,
    ) -> dict:
        async with self.session() as session:
            stmt = await session.execute(select(model).where(model.email == email))
            stmt = stmt.scalar()
            if stmt is None:
                user_model = PersonalData(
                    email=email,
                    first_name=new_model.first_name,
                    last_name=new_model.last_name,
                    dad_name=new_model.dad_name,
                    bio=new_model.bio,
                )
                session.add(user_model)
                await session.commit()
            else:
                for data, value in new_model.model_dump().items():
                    if value != "string":
                        setattr(stmt, data, value)
                    else:
                        continue
                await session.commit()
                return model

    async def read_data(self, model: PersonalData, email: str) -> dict | None:
        async with self.session() as session:
            stmt = select(model).where(model.email == email)
            result: Result = await session.execute(stmt)
            data = result.scalar()
            try:
                return data
            except Exception as _ex:
                return None
