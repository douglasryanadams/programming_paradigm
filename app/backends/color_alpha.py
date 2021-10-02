import aiohttp

from app.models.color import Color

BASE_URL = 'http://httpbin.org'


async def read(name: str) -> Color:
    async with aiohttp.ClientSession() as session:
        async with session.get(f'{BASE_URL}/get', params={'client': 'color:alpha', 'name': name}) as response:
            assert response.status == 200  # Stand-in for actual error handling
            print(await response.json())  # Stand in for business logic

            return Color(
                name='AlphaColor',
                red=50,
                green=50,
                blue=50
            )


async def write(color: Color) -> Color:
    async with aiohttp.ClientSession() as session:
        async with session.post(f'{BASE_URL}/post', data=color.dict()) as response:
            assert response.status == 200  # Stand-in for actual error handling
            print(await response.json())  # Stand in for business logic

            return Color(
                name='AlphaColor',
                red=50,
                green=50,
                blue=50
            )
