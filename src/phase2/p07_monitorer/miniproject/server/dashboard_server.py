from flask import Flask, request, jsonify, render_template_string
from datetime import datetime

app = Flask(__name__)
latest_metrics = {}

TEMPLATE = ""
@app.route("/metrics", methods=["POST"])
def receive_metrics():
    data = request.json
    data["timestamp"] = datetime.now().isoformat()
    latest_metrics[data["id"]] = data
    return jsonify(status="ok")

@app.route("/status")
def status():
    return jsonify(latest_metrics)

@app.route("/")
def dashboard():
    return render_template_string(TEMPLATE)

if __name__ == "__main__":
    with open("./template.html", "r", encoding="utf-8") as html:
        TEMPLATE = html.read()
    app.run(host="0.0.0.0", port=88, debug=True)


"""
pour du ssl : pip install pyopenssl
"""