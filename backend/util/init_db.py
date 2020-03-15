from db import get_db
from config import basedir
import os
import pymysql
import click


def init_db():
    db, _ = get_db()
    cursor = db.cursor()
    try:
        with open(os.path.join(basedir, 'init.sql'), mode='r', encoding="utf-8") as file:
            sql_commands = file.read().split(';')
            for sql_command in sql_commands:
                if sql_command.strip():
                    print(sql_command)
                    cursor.execute(sql_command)
        db.commit()
        return True
    except pymysql.err.Error:
        db.rollback()
        return False


@click.command('init-db')
def init_db_command():
    if init_db():
        click.echo('初始化完成')
    else:
        click.echo('初始化失败')


