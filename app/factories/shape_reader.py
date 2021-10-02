from typing import cast

from app.backends.abstract_shapes import AbstractShapeReader
from app.backends.shape_api_clients import AlphaClient, BetaClient
from app.backends.shape_alpha import AlphaShapeReader
from app.backends.shape_beta import BetaShapeManager
from app.factories.api_client import ApiClientFactory


class ShapeReaderFactory:

    def __init__(self, client_factory: ApiClientFactory):
        self._client_factory = client_factory

    async def get(self, backend: str) -> AbstractShapeReader:
        client = await self._client_factory.get(backend)
        if backend == 'alpha':
            alpha_client: AlphaClient = cast(AlphaClient, client)
            return AlphaShapeReader(alpha_client)
        if backend == 'beta':
            beta_client: BetaClient = cast(BetaClient, client)
            return BetaShapeManager(beta_client)
        raise Exception('Invalid backend')
