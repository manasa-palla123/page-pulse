from fastapi import FastAPI
from slowapi.middleware import SlowAPIMiddleware
from app.config import limiter
from app.routes.audit import router as audit_router

app = FastAPI(
    title="Page Pulse API",
    description="Production-grade URL Audit Service",
    version="1.0.0"
)

app.state.limiter = limiter
app.add_middleware(SlowAPIMiddleware)

app.include_router(audit_router)

@app.get("/")
async def root():
    return {
        "message": "Welcome to Page Pulse API",
        "status": "running"
    }