from flask import Flask
from flask_restful import Api
from api.resources.routes import init_routes
from flasgger import Swagger
from config import config as Config

api = Api()
swagger = Swagger(template_file='api_components.json', parse=True)
init_routes(api)


def create_app():
    app = Flask(__name__)
    config_name = 'dev'

    print(config_name)
    app.config.from_object(Config[config_name])

    Config[config_name].init_app(app)

    api.init_app(app)
    swagger.init_app(app)

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(port=5000)
