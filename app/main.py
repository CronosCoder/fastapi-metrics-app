import asyncio
from fastapi import FastAPI
from prometheus_client import make_asgi_app
from app.middleware.metrics_middleware import MetricsMiddleware
from app.routers import api, health
from app.tasks.background_tasks import system_metrics_task
from app.db import database

app = FastAPI()
app.add_middleware(MetricsMiddleware)

app.include_router(api.router)
app.include_router(health.router)

metrics_app = make_asgi_app()
app.mount("/metrics", metrics_app)

@app.on_event("startup")
async def startup():
    await database.connect()
    asyncio.create_task(system_metrics_task())

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

@app.get("/")
async def root():
    return {"message": "Welcome to FastAPI Monitoring System"}
