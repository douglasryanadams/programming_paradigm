from typing import cast

from app.backends.abstract_shapes import AbstractShapeWriter
from app.backends.api_clients import AlphaClient, BetaClient
from app.backends.shape_alpha import AlphaShapeWriter
from app.backends.shape_beta import BetaShapeManager
from app.factories.api_client import ApiClientFactory


class ShapeWriterFactory:

    def __init__(self, client_factory: ApiClientFactory):
        self._client_factory = client_factory

    async def get(self, backend: str) -> AbstractShapeWriter:
        client = await self._client_factory.get(backend)
        if backend == 'alpha':
            alpha_client: AlphaClient = cast(AlphaClient, client)
            return AlphaShapeWriter(alpha_client)
        if backend == 'beta':
            beta_client: BetaClient = cast(BetaClient, client)
            return BetaShapeManager(beta_client)
        raise Exception('Invalid backend')
