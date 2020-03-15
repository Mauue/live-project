from flask import Blueprint, jsonify

api = Blueprint('api', __name__, url_prefix="/api")


def make_response(data=None, code=0, msg=""):
    response = {
        'code': code,
        'msg': msg,
        'data': data
    }
    return jsonify(response)


from . import order, bg