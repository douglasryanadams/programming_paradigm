import random

from app.factories.shape_reader import ShapeReaderFactory
from app.factories.shape_writer import ShapeWriterFactory
from app.models.shape import Shape


class ShapeService:
    def __init__(
            self,
            shape_reader_factory: ShapeReaderFactory,
            shape_writer_factory: ShapeWriterFactory
    ):
        self._shape_reader_factory = shape_reader_factory
        self._shape_writer_factory = shape_writer_factory

    async def get(self, name: str) -> Shape:
        # Stand-in for logic that picks a backend
        backend = random.choice(['alpha', 'beta'])

        reader = await self._shape_reader_factory.get(backend)
        shape = await reader.read(name)
        return shape

    async def write(self, shape: Shape) -> Shape:
        backend = random.choice(['alpha', 'beta'])

        reader = await self._shape_writer_factory.get(backend)
        shape = await reader.write(shape)
        return shape
