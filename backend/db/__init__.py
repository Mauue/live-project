import pymysql
import logging
import config
from .Redis import _Redis

_db = None
Redis = None

try:
    _db = pymysql.Connect(config.DB_HOST, config.DB_USER, config.DB_PASSWORD, config.DB_DATABASE)
    Redis = _Redis()
    print(1)
except pymysql.Error as e:
    logging.error('数据库连接发生错误', e)


def get_db():
    cursor = _db.cursor(pymysql.cursors.DictCursor)
    return _db, cursor
