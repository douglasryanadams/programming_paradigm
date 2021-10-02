from app.backends.abstract_shapes import AbstractShapeReader, AbstractShapeWriter
from app.backends.api_clients import BetaClient
from app.models.shape import Shape


class BetaShapeManager(AbstractShapeReader, AbstractShapeWriter):

    def __init__(self, api_client: BetaClient):
        self._client = api_client

    async def read(self, name: str) -> Shape:
        response = await self._client.get(name)
        print(response)  # Stand in for business logic

        # translate response to object ...
        return Shape(
            name="BetaSquare",
            sides=4,
            side_lengths=[10, 10, 10, 10],
            corner_angles=[90.0, 90.0, 90.0, 90.0]
        )

    async def write(self, shape: Shape) -> Shape:
        response = await self._client.post(shape.dict())
        print(response)  # Stand in for business logic

        return Shape(
            name="BetaSquare",
            sides=4,
            side_lengths=[10, 10, 10, 10],
            corner_angles=[90.0, 90.0, 90.0, 90.0]
        )
