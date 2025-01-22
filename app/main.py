import asyncio
from contextlib import asynccontextmanager

from abcem.app.infrastructure.di.database import get_async_session
from abcem.app.infrastructure.jobs.schedulers import SchedulerService
from abcem.app.interfaces.api import router_all
from fastapi import FastAPI


app = FastAPI(docs_url= "/api/docs", redoc_url= "/api/redoc")

scheduler_service = SchedulerService()


app.include_router(router_all)

# Initialize Scheduler Service

@app.on_event("startup")
async def startup_event():
    async_session_generator =await get_async_session()
    async_session = await next(async_session_generator())  # Manually call dependency

    # Schedule the task




@app.on_event("shutdown")
async def shutdown_event():
    scheduler_service.stop()




