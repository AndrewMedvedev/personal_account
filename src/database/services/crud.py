from src.database.services.orm import DatabaseSessionService
from sqlalchemy import Result, delete, select


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

    async def read_data(self, model, email):
        async with self.session() as session:
            stmt = select(model).where(model.email == email)
            result: Result = await session.execute(stmt)
            data = result.scalars().all()
            try:
                return data
            except Exception as _ex:
                return None

    async def update_data(self, model, new_model, email):
        async with self.session() as session:
            stmt = await session.execute(select(model).where(model.email == email))
            for data, value in new_model.model_dump(exclude_unset=True).items():
                setattr(stmt, data, value)
                await session.commit()
                return model

    async def delete_user(self, model, email: str):
        async with self.session() as session:
            query = delete(model).where(model.email == email)
            cursor = await session.execute(query)
            await session.flush()