from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from slowapi.middleware import SlowAPIMiddleware
from app.config import limiter
from app.routes.audit import router as audit_router

app = FastAPI(
    title="Page Pulse API",
    description="Production-grade URL Audit Service",
    version="1.0.0"
)

# ADD THIS LINE
templates = Jinja2Templates(directory="app/templates")

app.state.limiter = limiter
app.add_middleware(SlowAPIMiddleware)

app.include_router(audit_router)

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html"
    )