from fastapi import FastAPI

from contextlib import asynccontextmanager
from app.api import ping, notes
from app.db import engine, database, metadata

# Create tables
metadata.create_all(engine)

app = FastAPI()

# Connect to DB on startup
@app.on_event("startup")
async def startup():
    await database.connect()

# Disconnect on shutdown
@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

# Include routers
app.include_router(ping.router)
app.include_router(notes.router, prefix="/notes", tags=["notes"])
