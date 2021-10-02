from fastapi import APIRouter

from app.models.color import Color
from app.services import color as color_service

router = APIRouter()


@router.get('/colors/{name}')
async def get_colors(name: str):
    return await color_service.get(name)


@router.post('/colors')
async def post_colors(color: Color):
    return await color_service.write(color)
