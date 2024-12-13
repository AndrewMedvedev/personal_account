from src.database.services.orm import DatabaseSessionService
from sqlalchemy import select


class CRUD(DatabaseSessionService):
    def __init__(self) -> None:
        super().__init__()
        self.init()

    async def create_data(self, model):
        async with self.session() as session:
            session.add(model)
            await session.commit()
            await session.refresh(model)
        return {"status": 200}

    async def read_data(self, model, email) -> list:
        async with self.session() as session:
            data = await session.execute(select(model).where(model.email == email))
            try:
                return model.scalars().all()
            except Exception as _ex:
                return None
