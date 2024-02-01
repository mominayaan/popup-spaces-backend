import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from config import load_config
from config.db import connect_db
from api import router as api_router

# Load configuration and database connection
config = load_config()
connect_db()

app = FastAPI(
    title="Neutrino",
    docs_url=None if config.ENV == "prod" else "/docs",
    redoc_url=None if config.ENV == "prod" else "/redoc",
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=config.CORS_ORIGIN_WHITELIST,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router, prefix="/api")


@app.get("/")
async def root():
    return {"message": "Hello from Neutrino"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=config.API_PORT)
