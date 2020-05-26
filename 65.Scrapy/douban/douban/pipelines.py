# -*- coding: utf-8 -*-
# from douban.settings import database_host, database_port, database_db_name, database_db_collection
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class DoubanPipeline:
    # 与数据库建立关系
    # def open_spider(self, spider):
    #     self.conn = pymysql.Connect(
    #         host=settings.MYSQL_HOST,
    #         database=...,
    #         port=...,
    #         user=...,
    #         password=...,
    #         charset='utf8'
    #     )
    #     创建游标对象
    #     self.cur = self.conn.cursor()
    # 插入数据
    def process_item(self, item, spider):
        # 这里的item就是爬虫爬取的数据
        # data = dict(item)

        # try:
        #     values = (
        #         None,
        #         item['name'],
        #         ...
        #     )
        #     sql = 'INSERT INTO tableName VALUES (%s ' + ',%s' * 8 + ')'
        #     self.cur.exexute(sql, values)
        #     # 提交sql语句
        #     self.conn.commit()
        # except Exception as e:
        #     print(e)
        #     self.conn.rollback()
        return item
    # 关闭数据库
    # def close_spider(self, spider):
    #     self.cur.close()
    #     self.conn.close()
