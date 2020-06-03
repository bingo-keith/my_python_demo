#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from models.model_xueya_articles import Article
import time

article = Article()


def get_all_articles():
    try:
        all_articles = article.get_all_articles()
        json_data = []
        for row in all_articles:
            res = {
                'id': row[0],
                'title': row[1],
                'category': row[2],
                'content': row[3],
                'author': row[4],
                'keywords': row[5],
                'stars': row[6],
                'readedNum': row[7],
                'favoritesNum': row[8],
                'sharedNum': row[9],
                'thumbNum': row[10],
                'isDeleted': row[11]
            }
            res['comments'] = get_comments_by_article_id(res)
            json_data.append(res)
        return json_data
    except Exception as e:
        raise e


def get_comments_by_article_id(articles):
    try:
        comments = article.get_comments_by_aid(articles['id'])
        json_data = []
        for row in comments:
            res = {
                'id': row[0],
                'avator': row[1],
                'content': row[2],
                'author': row[3],
                'thumbNum': row[4],
                'created': int(time.mktime(time.strptime(str(row[5]), "%Y-%m-%d %H:%M:%S"))) * 1000,
                'isDeleted': row[6]
            }
            json_data.append(res)
        return json_data
    except Exception as e:
        raise e
