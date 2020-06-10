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
            self.update_article_readed_num(aid, 1)
            self.conn.commit()
            return data
        except Exception as e:
            raise e
        finally:
            db_close()

    def update_article_readed_num(self, aid, step):
        try:
            sql = 'UPDATE xueya_articles SET a_readed_num = a_readed_num + %s WHERE a_id = %s' % (step, aid)
            self.cursor.execute(sql)
            self.conn.commit()
            return 'Success'
        except Exception as e:
            raise e
        finally:
            db_close()

    def update_article_star_num(self, aid, step):
        try:
            sql = 'UPDATE xueya_articles SET a_star = a_star + %s WHERE a_id = %s AND a_star >= %s'
            self.cursor.execute(sql, tuple([step, aid, 0 if step > 0 else 1]))
            self.conn.commit()
            return 'Success'
        except Exception as e:
            raise e
        finally:
            db_close()

    def update_article_shared_num(self, aid, step):
        try:
            sql = 'UPDATE xueya_articles SET a_shared_num = a_shared_num + %s WHERE a_id = %s AND a_shared_num >= %s'
            self.cursor.execute(sql, list([step, aid, 0 if step > 0 else 1]))
            self.conn.commit()
            return 'Success'
        except Exception as e:
            raise e
        finally:
            db_close()

    def update_article_thumb_num(self, aid, step):
        try:
            sql = 'UPDATE xueya_articles SET a_thumb_num = a_thumb_num + %s WHERE a_id = %s AND a_thumb_num >= %s'
            self.cursor.execute(sql, list([step, aid, 0 if step > 0 else 1]))
            self.conn.commit()
            return 'Success'
        except Exception as e:
            raise e
        finally:
            db_close()

