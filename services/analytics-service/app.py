from flask import Flask, jsonify, request
from prometheus_client import Counter, Histogram, generate_latest, CONTENT_TYPE_LATEST
import time
import random

app = Flask(__name__)

# Métricas
events_processed = Counter('events_processed_total', 'Total processed events')
events_failed = Counter('events_failed_total', 'Total failed events')
http_requests = Counter('http_requests_total', 'Total HTTP requests', ['method', 'endpoint'])
request_latency = Histogram('request_latency_seconds', 'Request latency')

@app.before_request
def before_request():
    request.start_time = time.time()

@app.after_request
def after_request(response):
    latency = time.time() - request.start_time
    request_latency.observe(latency)
    http_requests.labels(method=request.method, endpoint=request.path).inc()
    return response

@app.route("/health")
def health():
    return jsonify({"status": "ok", "service": "analytics-service"})

@app.route("/track")
def track():
    # Simular erro aleatório
    if random.random() < 0.2:
        events_failed.inc()
        return jsonify({"status": "error", "message": "simulated failure"}), 500

    events_processed.inc()
    return jsonify({"status": "ok", "message": "event tracked"})

@app.route("/metrics")
def metrics():
    return generate_latest(), 200, {'Content-Type': CONTENT_TYPE_LATEST}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8002)
