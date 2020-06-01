#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from mysql.connector import connect


class Users:
    def __init__(self, **kwargs):
        self.formData = {}
        for k, v in kwargs.items():
            self.formData[k] = v
        self.conn = connect(user='root', password='root', database='db_xueya_edu')
        self.cursor = self.conn.cursor()

    def get_all_users(self):
        self.cursor.execute('SELECT * FROM xueya_users')
        data = self.cursor.fetchall()
        self.conn.commit()
        self.db_close()
        return data

    def model_set_new_users(self, new_user):
        sql = '''INSERT INTO xueya_users
                VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'''
        self.cursor.execute(sql, list(new_user))
        self.conn.commit()
        self.db_close()

    def model_get_id_by_account_name(self, new_user):
        sql = 'SELECT u_id FROM xueya_users WHERE u_account_name = "%s"' % new_user[1]
        self.cursor.execute(sql)
        uid = self.cursor.fetchone()
        self.conn.commit()
        self.db_close()
        return uid[0]

    def db_close(self):
        # 关闭数据库
        self.cursor.close()
        self.conn.close()


