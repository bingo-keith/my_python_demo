#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from mysql.connector import connect
from config import user, password, database


def db_close():
    conn, cursor = db_conn()
    # 关闭数据库
    cursor.close()
    conn.close()


def db_conn():
    # 连接数据库
    conn = connect(user=user, password=password, database=database)
    cursor = conn.cursor()
    return conn, cursor
