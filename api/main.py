from fastapi import FastAPI

from config.logging_config import setup_logging
from config.settings import settings


logger = setup_logging(__name__)

app = FastAPI(
    title="MOSAIC API",
    description="Multi-agent clinical research intelligence system",
    version="0.1.0",
)


@app.on_event("startup")
async def startup_event():
    logger.info(
        "MOSAIC API starting | environment=%s | region=%s",
        settings.api_env,
        settings.gcp_region,
    )


@app.get("/")
async def root():
    logger.info("Root endpoint accessed")

    return {
        "name": "MOSAIC",
        "status": "running",
        "version": "0.1.0",
    }


@app.get("/health")
async def health():
    logger.info("Health check requested")

    return {
        "status": "healthy",
        "environment": settings.api_env,
    }