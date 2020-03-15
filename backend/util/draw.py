from db import get_db
import random


def draw_mask():
    db, cursor = get_db()
    cursor.execute("SELECT id, total, order_max FROM order_set WHERE status=0")
    order_round = cursor.fetchone()
    if order_round is None:
        return "没有未执行抽签的预约"

    cursor.execute("UPDATE order_set SET status=1 WHERE id=%s", order_round['id'])

    round_id = order_round['id']
    cursor.execute("SELECT phone, order_num FROM orders WHERE round_id=%s", round_id)
    orders = cursor.fetchall()
    if orders is None:
        db.commit()
        return None

    order_sum = 0
    for order in orders:
        order_sum += order['order_num']
    if order_sum <= order_round['total']:
        cursor.execute("UPDATE orders SET status=1 WHERE round_id=%s", round_id)
        db.commit()
        return None

    order_max = int(order_round['total']/order_round['order_max'])
    print(order_max)
    random.shuffle(orders)
    order_success = orders[0: order_max]
    print(order_success)
    order_phone_list = [i['phone'] for i in order_success]
    sql = "UPDATE orders SET status=1 " \
          "WHERE round_id=%s AND phone in (%s)" % (round_id, ','.join(['%s'] * len(order_success)))
    print(sql)
    cursor.execute(sql, order_phone_list)
    db.commit()
    return None


if __name__ == "__main__":
    db, cursor = get_db()
    cursor.execute("UPDATE orders set status=0")
    cursor.execute("UPDATE order_set set status=0")
    db.commit()
    print(draw_mask())