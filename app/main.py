from flask import Flask, jsonify, Response
import psutil
from prometheus_client import Gauge, generate_latest

app = Flask(__name__)

cpu_usage = Gauge(
    "devopsguard_cpu_usage_percent",
    "CPU usage percentage"
)

memory_usage = Gauge(
    "devopsguard_memory_usage_percent",
    "Memory usage percentage"
)

disk_usage = Gauge(
    "devopsguard_disk_usage_percent",
    "Disk usage percentage"
)

network_sent = Gauge(
    "devopsguard_network_sent_bytes",
    "Network bytes sent"
)

network_received = Gauge(
    "devopsguard_network_received_bytes",
    "Network bytes received"
)


@app.route("/")
def home():
    return "DevOpsGuard Monitoring System is Running"


@app.route("/health")
def health():
    return jsonify({
        "status": "healthy"
    })


@app.route("/metrics")
def metrics():
    cpu_usage.set(psutil.cpu_percent(interval=1))
    memory_usage.set(psutil.virtual_memory().percent)
    disk_usage.set(psutil.disk_usage("/").percent)

    network = psutil.net_io_counters()
    network_sent.set(network.bytes_sent)
    network_received.set(network.bytes_recv)

    return Response(
        generate_latest(),
        mimetype="text/plain"
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
