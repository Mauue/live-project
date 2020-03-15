from api import api, make_response
from flask import request
from db import get_db
import json
import time
import datetime


# @api.route('/order', methods=['POST', 'GET'])
def order_mask():
    if request.method == "POST":
        return new_order()
    return order_info()


def order_info():
    db, cursor = get_db()
    cursor.execute("SELECT * FROM order_set ORDER BY id DESC LIMIT 1")  # 只返回最新的一条记录
    data = cursor.fetchone()
    return make_response(data=data)


def new_order():
    name = request.form.get('name')
    if name is None:
        return make_response(msg="名字为空", code=111)
    phone = request.form.get('phone')
    if phone is None:
        return make_response(msg="电话号码为空", code=111)
    id_number = request.form.get('id_num')
    if id_number is None:
        return make_response(msg="电话号码为空", code=111)
    order_num = request.form.get('order_num')
    if id_number is None:
        return make_response(msg="订单数量为空", code=111)
    time_now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    sql1 = """SELECT * FROM order_set ORDER BY id DESC """
    db, cursor = get_db()
    cursor.execute(sql1)
    results = cursor.fetchall()
    for row in results:
        start_time = row[1]
        end_time = row[2]
        if (start_time < time_now) & (time_now < end_time):
            round_id = row[0]
            break

    sql2 = """INSERT INTO orders(round_id, phone, name, id_number,order_num)
         VALUES (%s, %s, %s, %s,%s)"""

    db, cursor = get_db()
    cursor.execute(sql2, (round_id, phone, name, id_number, order_num))
    return make_response(msg="插入订单项成功")


