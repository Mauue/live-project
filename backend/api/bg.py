import functools

from api import api, make_response
from flask import request, session
from db.admin import check_admin


@api.route('/bg/set_order')
def set_order():
    pass


@api.route('/bg/login', methods=['POST'])
def admin_login():
    username = request.form.get('username')
    password = request.form.get('password')
    if username is None or password is None:
        return make_response(msg="信息不完整", code=100)

    msg = check_admin(username, password)
    if msg:
        return make_response(msg=msg, code=200)
    session.clear()
    session['username'] = username
    return make_response(msg="登录成功")


def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        username = session.get('username')
        if username is None:
            return make_response(code=300, msg="需要管理员登录")
        return view(**kwargs)
    return wrapped_view


