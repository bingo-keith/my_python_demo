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


def get_articles_by_keywords(keyword):
    try:
        articles = article.get_articles_by_keyword(keyword['value'])
        json_data = []
        for row in articles:
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


def get_article_by_id(aid):
    try:
        articles = article.get_articles_by_id(aid)
        res = {
            'id': articles[0],
            'title': articles[1],
            'category': articles[2],
            'content': articles[3],
            'author': articles[4],
            'keywords': articles[5],
            'stars': articles[6],
            'readedNum': articles[7],
            'favoritesNum': articles[8],
            'sharedNum': articles[9],
            'thumbNum': articles[10],
            'isDeleted': articles[11]
        }
        res['comments'] = get_comments_by_article_id(res)
        return res
    except Exception as e:
        raise e


def set_comments(comments):
    try:
        return article.set_articles_comments(comments)
    except Exception as e:
        raise e


def update_star(aid, step):
    try:
        return article.update_article_star_num(aid, step)
    except Exception as e:
        raise e


def update_article_shared(aid, step):
    try:
        return article.update_article_shared_num(aid, step)
    except Exception as e:
        raise e


def update_article_thumb(aid, step):
    try:
        return article.update_article_thumb_num(aid, step)
    except Exception as e:
        raise e




