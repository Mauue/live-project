import functools

from api import api, make_response
from flask import request, session
from db.admin import check_admin


@api.route('/bg/set_order', methods=['POST'])
def set_order():
    start_time = request.form.get('start_time')
    end_time = request.form.get('end_time')
    total = request.form.get('total')
    order_max = request.form.get('order_max')

    if start_time is None:
        return make_response(msg="未设置开始日期")
    if end_time is None:
        return make_response(msg="未设置结束日期")
    if total is None:
        return make_response(msg="未设置总量")
    if order_max is None:
        return make_response(msg="未设置预约数量")

    db, cursor = get_db()
    cursor.execute("INSERT INTO order_set(start_time, end_time, total, order_max) "
                   "values (%s, %s, %s, %s)", (start_time, end_time, total, order_max))



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


