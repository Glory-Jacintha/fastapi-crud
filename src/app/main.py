from fastapi import FastAPI
from contextlib import asynccontextmanager

from app.api import ping
from app.db import engine, database, metadata


# Create tables
metadata.create_all(engine)


# Define lifespan event handler
@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup logic
    await database.connect()
    print("✅ Database connected")
    yield  # Application runs here
    # Shutdown logic
    await database.disconnect()
    print("🛑 Database disconnected")


# Pass lifespan handler to FastAPI
app = FastAPI(lifespan=lifespan)

# Include routers
app.include_router(ping.router)
