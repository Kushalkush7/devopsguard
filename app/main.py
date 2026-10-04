from flask import Flask, jsonify
import psutil

app = Flask(__name__)


@app.route("/")
def home():
    return "DevopsGuard CI Demo is Running"


@app.route("/health")
def health():
    return jsonify({
        "status": "healthy"
    })


@app.route("/metrics")
def metrics():

    data = {
        "cpu": psutil.cpu_percent(interval=1),
        "memory": psutil.virtual_memory().percent,
        "disk": psutil.disk_usage("/").percent,
        "network_sent": psutil.net_io_counters().bytes_sent,
        "network_received": psutil.net_io_counters().bytes_recv
    }

    return jsonify(data)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
