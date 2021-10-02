from abc import ABC, abstractmethod

from app.models.shape import Shape


class AbstractShapeReader(ABC):

    @abstractmethod
    async def read(self, name: str) -> Shape:
        ...


class AbstractShapeWriter(ABC):

    @abstractmethod
    async def write(self, shape: Shape):
        ...
