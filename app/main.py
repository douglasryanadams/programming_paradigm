from fastapi import FastAPI

from app.views import colors, shapes, symbols

app = FastAPI()
app.include_router(colors.router)
app.include_router(shapes.router)
app.include_router(symbols.router)
