from src.database.services.orm import DatabaseSessionService
from fastapi import HTTPException, status
from sqlalchemy import select


class CRUD(DatabaseSessionService):
    def __init__(self) -> None:
        super().__init__()
        self.init()

    async def create_user(self, model):
        async with self.session() as session:
            session.add(model)
            await session.commit()
            await session.refresh(model)
        return HTTPException(status_code=status.HTTP_200_OK)


    async def read_user(self, model):
        async with self.session() as session:
            data = session.execute(
                select(model).where(model.id == id).all()
            )
            try:
                