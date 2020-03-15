from flask import Flask
import backend.db

def create_app():
    _app = Flask(__name__)

    @_app.route('/')
    def index():
        return 'Hello World!'
    return _app


if __name__ == "__main__":
    app = create_app()
    app.run()

