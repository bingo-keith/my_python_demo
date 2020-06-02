#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from .common import db_conn, db_close


class User:
    def __init__(self, **kwargs):
        self.formData = {}
        for k, v in kwargs.items():
            self.formData[k] = v
        conn, cursor = db_conn()
        self.conn = conn
        self.cursor = cursor

    def get_all_users(self):
        self.cursor.execute('SELECT * FROM xueya_users')
        data = self.cursor.fetchall()
        self.conn.commit()
        db_close()
        return data

    def set_new_user(self, new_user):
        sql = '''INSERT INTO xueya_users
                VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'''
        self.cursor.execute(sql, list(new_user))
        self.conn.commit()
        db_close()

    def get_id_by_account_name(self, new_user):
        sql = 'SELECT u_id FROM xueya_users WHERE u_account_name = "%s"' % new_user[1]
        self.cursor.execute(sql)
        uid = self.cursor.fetchone()
        self.conn.commit()
        db_close()
        return uid[0]


