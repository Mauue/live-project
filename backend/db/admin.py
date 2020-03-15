from . import get_db
from werkzeug.security import *


def new_admin(username, password):
    db, cursor = get_db()
    cursor.execute("SELECT id FROM admin WHERE username=%s", username)
    user = cursor.fetchone()
    password = generate_password_hash(password)
    if user is None:
        try:
            cursor.execute("INSERT INTO admin(username, password) values (%s, %s)", (username, password))
            db.commit()
            return True, ""
        except Exception as e:
            db.rollback()
            return False, e
    return False, "用户名已存在"


def check_admin(username, password):
    db, cursor = get_db()
    cursor.execute("SELECT password FROM admin WHERE username=%s", username)
    user = cursor.fetchone()
    if user is None:
        return "账号不存在"
    if check_password_hash(user['password'], password):
        return None
    else:
        return "密码错误"

