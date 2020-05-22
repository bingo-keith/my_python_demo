# -*- coding: utf-8 -*-
# from douban.settings import database_host, database_port, database_db_name, database_db_collection
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class DoubanPipeline:
    # 这里把爬取到的数据通过管道保存到数据库里
    # def __init__(self):
    #     host = database_host
    #     ...
    def process_item(self, item, spider):
        # 这里的item就是爬虫爬取的数据
        # data = dict(item)
        return item
