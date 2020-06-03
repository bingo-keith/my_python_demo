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

    def get_favorites_by_user(self, user):
        try:
            sql = 'SELECT a.* FROM xueya_articles AS a, xueya_favorite__article AS f,' \
                  'xueya_users AS u WHERE a.a_id = f.a_id AND f.u_id = u.u_id AND' \
                  'u.u_account_name = "%s"' % user['u_account_name']
            self.cursor.execute(sql)
            favorites = self.cursor.fetchall()
            self.conn.commit()
        except Exception as e:
            raise e
        finally:
            db_close()
        return favorites

    def delete_user_by_uid(self, id_dict):
        try:
            # sql = 'DELETE FROM xueya_users WHERE u_id=%s' % id_dict['id']
            sql = 'UPDATE xueya_users SET is_deleted="Y" WHERE u_id="%s"' % id_dict['id']
            self.cursor.execute(sql)
            self.conn.commit()
            return id_dict['id']
        except Exception as e:
            raise e
        finally:
            db_close()


