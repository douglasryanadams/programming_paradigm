import random

import aiohttp
from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

ALPHA_BASE_URL = 'http://httpbin.org'
BETA_BASE_URL = 'http://httpbin.org'


class Symbol(BaseModel):
    name: str
    value: int


@router.get('/symbols/{name}')
async def get_symbols(name: str):
    # Stand-in for logic that picks a backend
    backend = random.choice(['alpha', 'beta'])

    if backend == 'alpha':
        async with aiohttp.ClientSession() as session:
            async with session.get(
                    f'{ALPHA_BASE_URL}/get',
                    params={'client': 'symbol:alpha', 'name': name}
            ) as response:
                assert response.status == 200  # Stand-in for actual error handling
                print(await response.json())  # Stand in for business logic

                return Symbol(
                    name='AlphaSymbol',
                    value=12
                )

    if backend == 'beta':
        async with aiohttp.ClientSession() as session:
            async with session.get(
                    f'{ALPHA_BASE_URL}/get',
                    params={'client': 'symbol:beta', 'name': name}
            ) as response:
                assert response.status == 200  # Stand-in for actual error handling
                print(await response.json())  # Stand in for business logic

                return Symbol(
                    name='BetaSymbol',
                    value=12
                )
    raise Exception('Invalid backend')


@router.post('/symbols')
async def post_symbols(symbol: Symbol):
    # Stand-in for logic that picks a backend
    backend = random.choice(['alpha', 'beta'])

    if backend == 'alpha':
        async with aiohttp.ClientSession() as session:
            async with session.post(
                    f'{ALPHA_BASE_URL}/post',
                    data=symbol.dict()
            ) as response:
                assert response.status == 200  # Stand-in for actual error handling
                print(await response.json())  # Stand in for business logic

                return Symbol(
                    name='AlphaSymbol',
                    value=12
                )

    if backend == 'beta':
        async with aiohttp.ClientSession() as session:
            async with session.post(
                    f'{ALPHA_BASE_URL}/post',
                    data=symbol.dict()
            ) as response:
                assert response.status == 200  # Stand-in for actual error handling
                print(await response.json())  # Stand in for business logic

                return Symbol(
                    name='BetaSymbol',
                    value=12
                )
    raise Exception('Invalid backend')
