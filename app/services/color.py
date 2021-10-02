import random

from app.models.color import Color


async def get(name: str) -> Color:
    # Stand-in for logic that picks a backend
    backend = random.choice(['alpha', 'beta'])

    if backend == 'alpha':
        from app.backends import color_alpha
        return await color_alpha.read(name)
    if backend == 'beta':
        from app.backends import color_beta
        return await color_beta.read(name)
    raise Exception('Invalid backend')


async def write(color: Color) -> Color:
    # Stand-in for logic that picks a backend
    backend = random.choice(['alpha', 'beta'])

    if backend == 'alpha':
        from app.backends import color_alpha
        return await color_alpha.write(color)
    if backend == 'beta':
        from app.backends import color_beta
        return await color_beta.write(color)
    raise Exception('Invalid backend')
