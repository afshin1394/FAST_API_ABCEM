from fastapi import FastAPI
from .interfaces.api import router_all as interfaces_router
app = FastAPI(docs_url= "/api/docs", redoc_url= "/api/redoc")

app.include_router(interfaces_router)