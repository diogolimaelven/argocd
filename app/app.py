from flask import Flask, render_template, request
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)
metrics = PrometheusMetrics(app)

@app.route("/")
def hello_world():

    return "nova versao"

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug = False)