import time
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from app.metrics.http_metrics import (
    http_requests_total, http_request_duration_seconds,
    request_size, response_size
)

class MetricsMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        start_time = time.time()
        response = await call_next(request)

        process_time = time.time() - start_time
        endpoint = request.url.path
        method = request.method
        status_code = str(response.status_code)

        http_requests_total.labels(method, endpoint, status_code).inc()
        http_request_duration_seconds.labels(endpoint, method).observe(process_time)
        request_size.labels(endpoint, method).observe(int(request.headers.get('content-length') or 0))
        response_size.labels(endpoint, method).observe(len(response.body) if hasattr(response, "body") else 0)

        return response
