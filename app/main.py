from fastapi import FastAPI, Request
from fastapi.responses import PlainTextResponse
import uuid
import logging
import os
from prometheus_client import Counter, generate_latest

# Logging setup
logger = logging.getLogger("shorty")
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
)

ENV = os.getenv("ENV", "local")

app = FastAPI()

# Metrics
shorten_counter = Counter("shorty_shorten_requests_total", "Total shorten requests")

# Correlation ID middleware
@app.middleware("http")
async def add_correlation_id(request: Request, call_next):
    request_id = request.headers.get("X-Request-ID", str(uuid.uuid4()))
    request.state.request_id = request_id
    response = await call_next(request)
    response.headers["X-Request-ID"] = request_id
    return response

# Health check
@app.get("/health")
def health():
    return {"status": "ok", "env": ENV}

# Metrics endpoint
@app.get("/metrics")
def metrics():
    return PlainTextResponse(generate_latest(), media_type="text/plain")

# Shorten URL
@app.post("/shorten")
async def shorten_url(url: str, request: Request):
    shorten_counter.inc()
    short_id = str(uuid.uuid4())[:8]

    logger.info(
        f"Short URL created | env={ENV} | request_id={request.state.request_id} | short_id={short_id}"
    )

    return {"short_id": short_id, "original_url": url}

# Redirect
@app.get("/{short_id}")
async def redirect(short_id: str, request: Request):
    logger.info(
        f"Redirect request | env={ENV} | request_id={request.state.request_id} | short_id={short_id}"
    )
    return {"message": f"Redirecting {short_id} (mock)"}
