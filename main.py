from flask import Flask, request
from flasgger import Swagger, LazyString, LazyJSONEncoder
from flasgger import swag_from

app = Flask(__name__)

app.json_encoder = LazyJSONEncoder

swagger_template = dict(
info = {
    'title': LazyString(lambda: 'Mock_Amplify'),
    'version': LazyString(lambda: 'v0'),
    'description': LazyString(lambda: 'Documentação da API Mockada para testes do Amplify Axway'),
    },
    host = LazyString(lambda: request.host)
)
swagger_config = {
    "headers": [],
    "specs": [
        {
            "endpoint": 'hello_world',
            "route": '/Hello_world.yml',
            "rule_filter": lambda rule: True,
            "model_filter": lambda tag: True,
        }
    ],
    "static_url_path": "/flasgger_static",
    "swagger_ui": True,
    "specs_route": "/apidoc/"
}

swagger = Swagger(app, template=swagger_template,             
                  config=swagger_config)


@swag_from("hello_world.yml", methods=['GET'])

@app.route('/hello_world')
def hello_world():
    return 'Hello World!'


app.run(host='localhost', port=5000)