import aiohttp
import pytest
from aiohttp import ClientSession

from app.models.color import Color
from app.models.shape import Shape


@pytest.fixture
async def client_session() -> ClientSession:
    async with aiohttp.ClientSession() as session:
        yield session


@pytest.mark.end_to_end
@pytest.mark.asyncio
async def test_read_shape(client_session):
    async with client_session.get('http://localhost:8000/shapes/square') as response:
        assert response.status == 200
        print(f'Read Shape Response: {await response.json()}')


@pytest.mark.end_to_end
@pytest.mark.asyncio
async def test_write_shape(client_session):
    shape = Shape(
        name='NewShape',
        sides=8,
        side_lengths=[2, 2, 2, 2, 2, 2, 2, 2],
        corner_angles=[45, 45, 45, 45, 45, 45, 45, 45]
    )
    async with client_session.post('http://localhost:8000/shapes', json=shape.dict()) as response:
        assert response.status == 200
        print(f'Write Shape Response: {await response.json()}')


@pytest.mark.end_to_end
@pytest.mark.asyncio
async def test_read_color(client_session):
    async with client_session.get('http://localhost:8000/colors/grey') as response:
        assert response.status == 200
        print(f'Read Shape Response: {await response.json()}')


@pytest.mark.end_to_end
@pytest.mark.asyncio
async def test_write_color(client_session):
    color = Color(
        name='NewColor',
        red=0,
        blue=0,
        green=255
    )
    async with client_session.post('http://localhost:8000/colors', json=color.dict()) as response:
        assert response.status == 200
        print(f'Write Shape Response: {await response.json()}')
