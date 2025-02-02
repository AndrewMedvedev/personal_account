from src.database.services.orm import DatabaseSessionService
from sqlalchemy import Result, select
from src.database.models import PersonalData


class CRUD(DatabaseSessionService):
    def __init__(self) -> None:
        super().__init__()
        self.init()

    async def add_or_update_data_email(self, user: PersonalData, email: str) -> None:
        async with self.session() as session:
            stmt = select(PersonalData).where(PersonalData.email == email)
            user_from_db = await session.execute(stmt)
            if user_from_db.scalar_one_or_none() is None:
                session.add(user)
                await session.commit()
                await session.refresh(user)
            else:
                await session.merge(user)
                await session.commit()
                await session.refresh(user)

    async def read_data(self, model: PersonalData, email: str) -> dict | None:
        async with self.session() as session:
            stmt = select(model).where(model.email == email)
            result: Result = await session.execute(stmt)
            data = result.scalar()
            try:
                return data
            except Exception as _ex:
                return None
