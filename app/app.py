from flask import Flask, render_template, request
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)
metrics = PrometheusMetrics(app)

@app.route("/")
def hello_world():

    return "gg du bom!"

@app.route("/cadastro")
def cadastro():

    return "cadastro"

@app.route("/produto")
def produto():

    return "produto"


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug = False)
