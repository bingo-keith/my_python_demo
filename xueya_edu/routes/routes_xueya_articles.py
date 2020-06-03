#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import jsonify, Blueprint, request
from json import dumps
from services.services_xueya_articles import get_all_articles, get_comments_by_article_id, get_articles_by_keywords

# 注册蓝图
r_articles = Blueprint('articles', __name__)


@r_articles.route('/api/v1/getAllArticles/', methods=['GET'])
def get_articles():
    return jsonify(get_all_articles())


@r_articles.route('/api/v1/getCommentsById/', methods=['GET'])
def get_comments_by_id():
    return jsonify(get_comments_by_article_id(dict(request.args)))


@r_articles.route('/api/v1/getArticlesByKeyword', methods=['GET'])
def get_by_keywords():
    return jsonify(get_articles_by_keywords(dict(request.args)))
