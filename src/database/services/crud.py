from src.database.services.orm import DatabaseSessionService
from sqlalchemy import Result, select


class CRUD(DatabaseSessionService):
    def __init__(self) -> None:
        super().__init__()
        self.init()

    async def create_data(self, model) -> dict:
        async with self.session() as session:
            session.add(model)
            await session.commit()
            await session.refresh(model)
        return {"status": 200}

    async def read_data(self, model, email: str) -> dict | None:
        async with self.session() as session:
            stmt = select(model).where(model.email == email)
            result: Result = await session.execute(stmt)
            data = result.scalar()
            try:
                return data
            except Exception as _ex:
                return None

    async def update_data_email(self, model, new_model, email: str) -> dict:
        async with self.session() as session:
            stmt = await session.execute(select(model).where(model.email == email))
            stmt = stmt.scalar()
            for data, value in new_model.model_dump().items():
                if value != "string":
                    setattr(stmt, data, value)
                else:
                    continue
            await session.commit()
            return model

    async def update_data_id_vk(self, model, new_model, id_vk: int) -> dict:
        async with self.session() as session:
            stmt = await session.execute(select(model).where(model.id_vk == id_vk))
            stmt = stmt.scalar()
            for data, value in new_model.model_dump().items():
                if value != "string":
                    setattr(stmt, data, value)
                else:
                    continue
            await session.commit()
            return model
