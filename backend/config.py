
DB_HOST = 'localhost'
DB_USER = 'root'
DB_PASSWORD = '123456'
DB_DATABASE = 'order_mask'

REDIS_HOST = 'localhost'
REDIS_PORT = '6379'
REDIS_PASSWORD = None
REDIS_DB = 0
REDIS_PREFIX = 'ISW:'

try:
    import os, sys, traceback
    if os.path.exists(os.path.join(os.path.dirname(__file__), 'config_local.py')):
        from config_local import *

except ImportError as e:
    print('Load local config failed')

