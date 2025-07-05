from prometheus_client import Counter, Histogram

http_requests_total = Counter(
    "http_requests_total", "Total HTTP requests",
    ["method", "endpoint", "status_code"]
)

http_request_duration_seconds = Histogram(
    "http_request_duration_seconds", "HTTP request latency",
    ["endpoint", "method"]
)

request_size = Histogram(
    "http_request_size_bytes", "Request size in bytes",
    ["endpoint", "method"]
)

response_size = Histogram(
    "http_response_size_bytes", "Response size in bytes",
    ["endpoint", "method"]
)
