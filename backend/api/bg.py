import functools
import time

from api import api, make_response
from flask import request, session
from db.admin import check_admin
from db import get_db
from datetime import datetime


@api.route('/bg/order/set', methods=['POST'])
def set_order():
    current_time = datetime.now()
    start_time = request.form.get('start_time')
    end_time = request.form.get('end_time')
    total = request.form.get('total', type=int)
    order_max = request.form.get('order_max', type=int)

    if start_time is None:
        return make_response(msg="未设置开始日期", code=100)
    if end_time is None:
        return make_response(msg="未设置结束日期", code=100)
    if total is None:
        return make_response(msg="未设置总量", code=100)
    if order_max is None:
        return make_response(msg="未设置预约数量", code=100)
    try:
        start_time = datetime.strptime(start_time, "%Y-%m-%d %H:%M:%S")
        end_time = datetime.strptime(end_time, "%Y-%m-%d %H:%M:%S")
    except ValueError:
        return make_response(msg="日期格式错误", code=200)
    if start_time < current_time or start_time > end_time or \
            order_max > total or total < 1 or order_max < 1:
        return make_response(msg="设置信息错误", code=201)

    db, cursor = get_db()
    cursor.execute("SELECT id FROM order_set WHERE status=0")
    if cursor.fetchone() is not None:
        return make_response(msg="存在未进行抽签的预约", code=300)

    cursor.execute("INSERT INTO order_set(start_time, end_time, total, order_max) "
                   "values (%s, %s, %s, %s)", (start_time, end_time, total, order_max))
    db.commit()
    return make_response(msg="设置成功")


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


