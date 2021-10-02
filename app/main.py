from fastapi import FastAPI

from app.views import colors, shapes

app = FastAPI()
app.include_router(colors.router)
app.include_router(shapes.router)
