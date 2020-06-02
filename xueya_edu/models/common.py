#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from mysql.connector import connect


def db_close():
    conn, cursor = db_conn()
    # 关闭数据库
    cursor.close()
    conn.close()


def db_conn():
    # 连接数据库
    conn = connect(user='root', password='root', database='db_xueya_edu')
    cursor = conn.cursor()
    return conn, cursor
