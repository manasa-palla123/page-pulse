from fastapi import APIRouter, Request
from app.schemas.audit import AuditRequest
from app.services.audit_service import audit_website
from app.config import limiter

router = APIRouter(
    prefix="/audit",
    tags=["Audit"]
)


@router.post("/")
@limiter.limit("10/minute")
async def audit_url(request: Request, body: AuditRequest):
    return await audit_website(str(body.url))