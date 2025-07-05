import asyncio
from app.metrics.system_metrics import collect_system_metrics
from app.config import METRIC_COLLECTION_INTERVAL

async def system_metrics_task():
    while True:
        collect_system_metrics()
        await asyncio.sleep(METRIC_COLLECTION_INTERVAL)
