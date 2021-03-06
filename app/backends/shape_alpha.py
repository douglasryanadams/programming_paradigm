from app.backends.abstract_shapes import AbstractShapeReader, AbstractShapeWriter
from app.backends.shape_api_clients import AlphaClient
from app.models.shape import Shape


class AlphaShapeReader(AbstractShapeReader):

    def __init__(self, api_client: AlphaClient):
        self._client = api_client

    async def read(self, name: str) -> Shape:
        response = await self._client.get(name)
        print(response)  # Stand-in for business logic

        # translate response to object ...
        return Shape(
            name="AlphaSquare",
            sides=4,
            side_lengths=[10, 10, 10, 10],
            corner_angles=[90.0, 90.0, 90.0, 90.0]
        )


class AlphaShapeWriter(AbstractShapeWriter):

    def __init__(self, api_client: AlphaClient):
        self._client = api_client

    async def write(self, shape: Shape) -> Shape:
        response = await self._client.post(shape.dict())
        print(response)  # Stand in for business logic

        # translate response to object ...
        return Shape(
            name="AlphaSquare",
            sides=4,
            side_lengths=[10, 10, 10, 10],
            corner_angles=[90.0, 90.0, 90.0, 90.0]
        )
