from backend.config import *
import pymysql
import logging


try:
    _db = pymysql.Connect(DB_HOST, DB_USER, DB_PASSWORD, DB_DATABASE)
except pymysql.Error as e:
    logging.error('数据库连接发生错误', e)


def get_db():
    return _db
