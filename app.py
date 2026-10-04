from flask import Flask, jsonify
import os

app = Flask(__name__)


@app.route("/")
def home():
    return jsonify({
        "message": "Hello from Kubernetes!",
        "environment": os.getenv("ENVIRONMENT", "dev")
    })


@app.route("/health")
def health():
    return jsonify({
        "status": "healthy"
    })


@app.route("/info")
def info():
    return jsonify({
        "application": "student-k8s-app",
        "version": "1.0"
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)