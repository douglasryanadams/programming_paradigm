from abc import ABC, abstractmethod
from typing import Dict

from aiohttp import ClientSession


class Client(ABC):

    @abstractmethod
    async def get(self, name: str) -> Dict:
        ...

    @abstractmethod
    async def post(self, data: Dict) -> Dict:
        ...


class AlphaClient(Client):

    def __init__(self, base_url: str, session: ClientSession):
        self._base_url = base_url
        self._session = session

    async def get(self, name: str) -> Dict:
        async with self._session.get(f'{self._base_url}/get', params={'client': 'shape:alpha', 'name': name}) as response:
            assert response.status == 200  # Stand-in for actual error handling
            return await response.json()

    async def post(self, data: Dict) -> Dict:
        async with self._session.post(f'{self._base_url}/post', data=data) as response:
            assert response.status == 200
            return await response.json()


class BetaClient(Client):

    def __init__(self, base_url: str, session: ClientSession):
        self._base_url = base_url
        self._session = session

    async def get(self, name) -> Dict:
        async with self._session.get(f'{self._base_url}/get', params={'client': 'shape:beta', 'name': name}) as response:
            assert response.status == 200
            return await response.json()

    async def post(self, data: Dict) -> Dict:
        async with self._session.post(f'{self._base_url}/post', data=data) as response:
            assert response.status == 200
            return await response.json()
