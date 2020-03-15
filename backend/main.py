from flask import Flask
from api import api
import db

def create_app():
    _app = Flask(__name__)

    @_app.route('/')
    def index():
        return 'Hello World!'

    _app.register_blueprint(api)

    return _app


if __name__ == "__main__":
    app = create_app()
    app.run()

