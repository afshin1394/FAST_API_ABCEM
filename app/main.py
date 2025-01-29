

from abcem.app.infrastructure.jobs.schedulers import SchedulerService
from abcem.app.infrastructure.postgres import initialize_database
from abcem.app.interfaces.api import router_all
from fastapi import FastAPI


app = FastAPI(docs_url= "/api/docs", redoc_url= "/api/redoc")

scheduler_service = SchedulerService()


app.include_router(router_all)

# Initialize Scheduler Service

@app.on_event("startup")
async def startup_event():
    print("dadasdsadsadsdad")
    await initialize_database()


@app.on_event("shutdown")
async def shutdown_event():
    pass
    # scheduler_service.stop()




