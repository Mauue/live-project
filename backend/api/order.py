from api import api, make_response
from flask import request
from db import get_db
import json


@api.route('/order', methods=['POST', 'GET'])
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
    return ""

