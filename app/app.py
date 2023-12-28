from flask import Flask, render_template, request
from prometheus_flask_exporter import PrometheusMetrics
from elasticapm.contrib.flask import ElasticAPM

import os

app = Flask(__name__)
apm = ElasticAPM(app)
metrics = PrometheusMetrics(app)
app.config['ELASTIC_APM'] = {
  # Set the required service name. Allowed characters:
  # a-z, A-Z, 0-9, -, _, and space
  #'SERVICE_NAME': 'my-service-name',

  # Use if APM Server requires a secret token
  'SECRET_TOKEN': '',

  # Set the custom APM Server URL (default: http://localhost:8200)
  'SERVER_URL': 'http://localhost:8200',

  # Set the service environment
  'ENVIRONMENT': 'my-environment',
}

apm = ElasticAPM(app)


@app.route("/")
def hello_world():

    return "teste caramelo e siajo"

@app.route("/cadastro")
def cadastro():

    return "cadastro"

@app.route("/produto")
def produto():

    return "produto"

@app.route("/segredo")
def get_env_value():
    usuario = os.environ['usuario']
    # senha = os.environ['senha']
    return usuario #, senha
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug = False)
