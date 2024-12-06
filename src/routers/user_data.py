from ast import stmt
from fastapi import APIRouter
from src.database.schemas import AllData
from src.database.services.crud import CRUD
from src.database.models import PersonalData, Recomendate
router = APIRouter(prefix='/user_data', tags='user_data')



@router.post('/')
async def post_data(model: AllData):
    stmt = await CRUD().create_data(PersonalData)
    