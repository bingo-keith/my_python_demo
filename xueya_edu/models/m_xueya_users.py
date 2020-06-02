#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from .common import db_conn, db_close


class User:
    def __init__(self, **kwargs):
        self.formData = {}
        for k, v in kwargs.items():
            self.formData[k] = v
        try:
            conn, cursor = db_conn()
            self.conn = conn
            self.cursor = cursor
        except Exception as e:
            raise e

    def get_all_users(self):
        try:
            self.cursor.execute('SELECT * FROM xueya_users')
            data = self.cursor.fetchall()
            self.conn.commit()
            return data
        except Exception as e:
            raise e
        finally:
            db_close()

    def set_new_user(self, new_user):
        try:
            sql = '''INSERT INTO xueya_users
                    VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'''
            self.cursor.execute(sql, list(new_user))
            self.conn.commit()
        except Exception as e:
            raise e
        finally:
            db_close()

    def get_id_by_account_name(self, new_user):
        try:
            sql = 'SELECT u_id FROM xueya_users WHERE u_account_name = "%s"' % new_user[1]
            self.cursor.execute(sql)
            uid = self.cursor.fetchone()
            self.conn.commit()
        except Exception as e:
            raise e
        finally:
            db_close()
        return uid[0]


