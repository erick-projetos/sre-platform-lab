from flask import Flask
from prometheus_client import Counter, Histogram, generate_latest, CONTENT_TYPE_LATEST
import time
import random

# 🔥 OpenTelemetry
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter
from opentelemetry.instrumentation.flask import FlaskInstrumentor
from opentelemetry.sdk.resources import Resource
from opentelemetry.trace import get_current_span

resource = Resource.create({
    "service.name": "sre-platform-app"
})

trace.set_tracer_provider(TracerProvider(resource=resource))


tracer = trace.get_tracer(__name__)

def get_trace_id():
    span = get_current_span()
    ctx = span.get_span_context()

    if ctx and ctx.trace_id != 0:
        return format(ctx.trace_id, '032x')
    return "no-trace"

otlp_exporter = OTLPSpanExporter(endpoint="http://tempo:4317", insecure=True)
span_processor = BatchSpanProcessor(otlp_exporter)
trace.get_tracer_provider().add_span_processor(span_processor)

app = Flask(__name__)
FlaskInstrumentor().instrument_app(app)

REQUESTS = Counter('http_requests_total', 'Total Requests', ['status', 'endpoint', 'method'])
ERRORS = Counter('http_request_errors_total', 'Errors', ['endpoint'])
LATENCY = Histogram('request_duration_seconds', 'Request Latency', ['endpoint'])

@app.route('/')
def home():
    with tracer.start_as_current_span("home-request"):
        trace_id = get_trace_id()
        print(f"request received trace_id={trace_id}")

        REQUESTS.labels(status="200", endpoint="/", method="GET").inc()
        start = time.time()
        time.sleep(random.random())
        LATENCY.labels(endpoint="/").observe(time.time() - start)
        return "OK"

@app.route('/error')
def error():
    with tracer.start_as_current_span("error-endpoint"):
        trace_id = get_trace_id()
        print(f"error occurred trace_id={trace_id}")

        start = time.time()
        time.sleep(random.uniform(0.5, 2))

        LATENCY.labels(endpoint="/error").observe(time.time() - start)
        REQUESTS.labels(status="500", endpoint="/error", method="GET").inc()
        ERRORS.labels(endpoint="/error").inc()
        return "Error", 500

@app.route('/metrics')
def metrics():
    return generate_latest(), 200, {'Content-Type': CONTENT_TYPE_LATEST}


@app.route('/health')
def health():
    return "OK", 200
@app.route('/load')
def load():
    for _ in range(1000):
        pass
    return "Load Generated"
if __name__ == "__main__":
     app.run(host='0.0.0.0', port=5000)
