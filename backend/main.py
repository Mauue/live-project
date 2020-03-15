from flask import Flask


def create_app():
    _app = Flask(__name__)
    return _app


if __name__ == "__main__":
    app = create_app()
    app.run()

