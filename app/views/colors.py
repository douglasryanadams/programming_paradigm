from fastapi import APIRouter

router = APIRouter()


@router.get('/colors')
async def get_colors():
    ...


@router.post('/colors')
async def post_colors():
    ...
