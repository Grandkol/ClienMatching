import uvicorn
from fastapi import FastAPI
from fastapi.responses import ORJSONResponse
from contextlib import asynccontextmanager

from core.config import settings
from db import db_helper




@asynccontextmanager
async def lifespan(app: FastAPI):

    yield

    await db_helper.dispose()



app = FastAPI(
    title=settings.project_name,
    docs_url="/api/openapi",
    openapi_url="/api/openapi.json",
    default_response_class=ORJSONResponse,
    lifespan=lifespan,
)


# app.include_router(auth.router, prefix="/api/v1/auth", tags=["auth"])

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host=settings.run_config.host,
        port=settings.run_config.port,
        reload=True,
    )