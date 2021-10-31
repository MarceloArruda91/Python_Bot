from fastapi import FastAPI
from routers.router import router as api


# Iniciar API

def app_start() -> FastAPI:
    app = FastAPI()
    app.include_router(api)
    return app


app = app_start
