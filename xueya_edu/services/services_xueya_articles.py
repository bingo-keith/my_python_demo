#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from models.model_xueya_articles import Article

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
                'readedNum': row[6],
                'favoritesNum': row[7],
                'sharedNum': row[8],
                'thumbNum': row[9],
                'isDeleted': row[10]
            }
            json_data.append(res)
        return json_data
    except Exception as e:
        raise e


def get_comments_by_article_id(articles):
    try:
        comments = article.get_comments_by_aid(articles['id'])
        print(comments)
        json_data = []
        for row in comments:
            res = {
                'id': row[0],
                'avator': row[1],
                'content': row[2],
                'author': row[3],
                'thumbNum': row[4],
                'created': row[5],
                'isDeleted': row[6]
            }
            json_data.append(res)
        return json_data
    except Exception as e:
        raise e
