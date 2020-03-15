from flask import Flask
from api import api
import db
from util.register_admin import register_admin
from util.init_db import init_db_command


def create_app():
    _app = Flask(__name__)

    @_app.route('/')
    def index():
        return 'Hello World!'

    _app.config.from_mapping(
        SECRET_KEY='dev'
    )
    _app.register_blueprint(api)
    init_app(_app)

    return _app


def init_app(app):
    app.cli.add_command(register_admin)
    app.cli.add_command(init_db_command)


if __name__ == "__main__":
    app = create_app()
    app.run()

