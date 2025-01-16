from fastapi import FastAPI

from app.interfaces.api import router_all

app = FastAPI(docs_url= "/api/docs", redoc_url= "/api/redoc")

app.include_router(router_all)