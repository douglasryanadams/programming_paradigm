from contextlib import asynccontextmanager
from typing import AsyncGenerator

import aiohttp
from fastapi import APIRouter

from app.factories.api_client import ApiClientFactory
from app.factories.shape_reader import ShapeReaderFactory
from app.factories.shape_writer import ShapeWriterFactory
from app.models.shape import Shape
from app.services.shape import ShapeService

router = APIRouter()


@asynccontextmanager
async def _get_service() -> AsyncGenerator[ShapeService, None]:
    session = aiohttp.ClientSession()
    try:
        client_factory = ApiClientFactory(
            base_url_dict={
                'alpha': 'http://httpbin.org',
                'beta': 'http://httpbin.org'  # These could be different in a real app
            },
            session=session,
        )
        shape_reader_factory = ShapeReaderFactory(client_factory)
        shape_writer_factory = ShapeWriterFactory(client_factory)
        service = ShapeService(shape_reader_factory, shape_writer_factory)
        yield service
    finally:
        await session.close()


@router.get('/shapes/{name}')
async def get_colors(name: str):
    async with _get_service() as service:
        return await service.get(name)


@router.post('/shapes')
async def post_colors(shape: Shape):
    async with _get_service() as service:
        return await service.write(shape)
