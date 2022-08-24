from flask import Flask, render_template, request
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)
metrics = PrometheusMetrics(app)

@app.route("/")
def hello_world():

    return "App fabs"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3003, debug = False)
