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

    '''没有用到'''
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

    def set_articles_comments(self, comments):
        try:
            sql = 'INSERT INTO xueya_comments VALUES(%s, %s, %s, %s, %s, %s, %s)'
            self.cursor.execute(sql, (None, None, comments['content'], comments['author'], 0, None, 'N'))
            self.conn.commit()
            last_id = self.cursor.lastrowid
            sql2 = 'INSERT INTO xueya_articles__comments VALUES(NULL, %s, %s);' % (comments['id'], last_id)
            self.cursor.execute(sql2)
            self.conn.commit()
            return last_id
        except Exception as e:
            raise e
        finally:
            db_close()

    def get_articles_by_id(self, aid):
        try:
            sql = 'SELECT * FROM xueya_articles WHERE a_id = %s' % aid
            self.cursor.execute(sql)
            data = self.cursor.fetchone()
            self.conn.commit()
            # sql2 = 'SELECT c.* FROM xueya_comments as c, xueya_articles__comments as ac WHERE c.c_id = ac.ac_id ' \
            #        'AND ac. a_id = %s' % aid
            # self.cursor.execute(sql2)
            # comments = self.cursor.fetchall()
            # self.conn.commit()
            # data['comments'] = comments
            return data
        except Exception as e:
            raise e
        finally:
            db_close()



