#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from .common import db_conn, db_close


class Article:
    def __init__(self, **kwargs):
        self.formData = {}
        for k, v in kwargs:
            self.formData[k] = v
        try:
            conn, cursor = db_conn()
            self.conn = conn
            self.cursor = cursor
        except Exception as e:
            raise e

    def get_all_articles(self):
        try:
            sql = 'SELECT * FROM xueya_articles WHERE is_deleted="N"'
            self.cursor.execute(sql)
            data = self.cursor.fetchall()
            self.conn.commit()
            return data
        except Exception as e:
            raise e
        finally:
            db_close()

    def get_comments_by_aid(self, a_id):
        try:
            sql = '''SELECT c.* 
                FROM 
                    xueya_articles as a,
                    xueya_articles__comments as ac,
                    xueya_comments as c 
                WHERE
                    a.a_id = ac.a_id 
                    AND ac.c_id = c.c_id 
                    AND a.a_id = %s
            ''' % a_id
            self.cursor.execute(sql)
            data = self.cursor.fetchall()
            self.conn.commit()
            return data
        except Exception as e:
            raise e
        finally:
            db_close()

    def get_articles_by_keyword(self, keyword):
        try:
            sql = '''SELECT * FROM xueya_articles WHERE
                    a_category LIKE "%%%s%%"
                OR a_title LIKE "%%%s%%"
                OR a_content LIKE "%%%s%%"
                OR a_keywords LIKE "%%%s%%" 
            ''' % (keyword, keyword, keyword, keyword)
            self.cursor.execute(sql)
            data = self.cursor.fetchall()
            self.conn.commit()
            return data
        except Exception as e:
            raise e
        finally:
            db_close()
