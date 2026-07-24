import time
import httpx

from app.utils.cache import cache
from app.utils.request_id import generate_request_id
from app.utils.logger import logger




async def audit_website(url: str):
    request_id = generate_request_id()

    logger.info(f"RequestID={request_id} | Incoming URL={url}")

    # Check cache first
    if url in cache:
        cached = cache[url].copy()
        cached["cached"] = True
        cached["request_id"] = request_id

        logger.info(f"RequestID={request_id} | Cache Hit")

        return cached

    start_time = time.perf_counter()

    try:
        async with httpx.AsyncClient(timeout=5.0, follow_redirects=True) as client:
            response = await client.get(url)

        response_time = round((time.perf_counter() - start_time) * 1000, 2)

        result = {
            "request_id": request_id,
            "success": True,
            "url": str(response.url),
            "status_code": response.status_code,
            "response_time_ms": response_time,
            "content_type": response.headers.get("content-type"),
            "server": response.headers.get("server"),
            "cached": False
        }

        # Store in cache
        cache[url] = result

        logger.info(
            f"RequestID={request_id} | Success | Status={response.status_code} | Time={response_time}ms"
        )

        return result

    except httpx.TimeoutException:
        logger.error(f"RequestID={request_id} | TIMEOUT | URL={url}")

        return {
            "request_id": request_id,
            "success": False,
            "error": {
                "code": "TIMEOUT",
                "message": "Website took too long to respond."
            }
        }

    except Exception as e:
        logger.error(f"RequestID={request_id} | ERROR={str(e)}")

        return {
            "request_id": request_id,
            "success": False,
            "error": {
                "code": "REQUEST_FAILED",
                "message": str(e)
            }
        }