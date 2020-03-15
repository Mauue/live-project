from api import api, make_response
from flask import request
from db import get_db
import json
import time
import datetime


@api.route('/order', methods=['POST', 'GET'])
def order_mask():
    if request.method == "POST":
        return new_order()
    return order_info()


def order_info():
    db, cursor = get_db()
    cursor.execute("SELECT * FROM order_set ORDER BY id DESC LIMIT 1")  # 只返回最新的一条记录
    data = cursor.fetchone()
    data['start_time'] = data['start_time'].strftime('%Y-%m-%d %H:%M:%S')
    data['end_time'] = data['end_time'].strftime('%Y-%m-%d %H:%M:%S')
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
    sql1 = """SELECT id FROM order_set WHERE status=0 """
    db, cursor = get_db()
    cursor.execute(sql1)
    round_id = cursor.fetchone()[0]

    sql2 = """INSERT INTO orders(round_id, phone, name, id_number,order_num)
         VALUES (%s, %s, %s, %s,%s)"""

    cursor.execute(sql2, (round_id, phone, name, id_number, order_num))
    db.commit()
    return make_response(msg="插入订单项成功")


@api.route('/order/<int:id>')
def get_order_status(id):
    db, cursor = get_db()
    sql = "SELECT o.name, o.phone, o.order_num, o.id_number, os.status as round_status" \
          " FROM orders o INNER JOIN order_set os on o.round_id = os.id" \
          " WHERE o.id=%s"
    cursor.execute(sql, id)
    record = cursor.fetchone()
    if record is None:
        return make_response(msg="预约编号不存在", code=100)

    if record['round_status'] == 0:
        return make_response(msg="抽签未开始", code=200)
    record.pop('round_status')

    name_len = len(record['name'])
    if name_len < 3:
        record['name'] = record['name'][0] + '*'
    else:
        record['name'] = record['name'][0] + '*'*(name_len-2) + record['name'][-1]
    try:
        record['phone'] = record['phone'][0:3] + '*'*4 + record['phone'][7:11]
        record['id_number'] = record['id_number'][0:5] + '*'*9 + record['id_number'][-4:]
    except IndexError:
        pass
    return make_response(data=record)