from fastapi import APIRouter
import asyncio
import aiohttp


router = APIRouter(prefix='/recomendate', tags='recomendate')


async def send_data():
    