from typing import Union, Dict

from aiohttp import ClientSession

from app.backends.api_clients import BetaClient, AlphaClient


class ApiClientFactory:
    def __init__(self, base_url_dict: Dict[str,str], session: ClientSession):
        self._base_url_dict = base_url_dict
        self._session = session

    async def get(self, backend: str) -> Union[AlphaClient, BetaClient]:
        if backend == 'alpha':
            return AlphaClient(base_url=self._base_url_dict['alpha'], session=self._session)
        if backend == 'beta':
            return BetaClient(base_url=self._base_url_dict['beta'], session=self._session)
        raise Exception('Invalid backend')
