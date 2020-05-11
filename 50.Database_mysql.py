#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 导入mysql驱动
import mysql.connector
# 连接数据库
conn = mysql.connector.connect(user='root', password='root', database='test')
cursor = conn.cursor()
# 创建user表
cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
# 插入数据
cursor.execute('insert into user (id, name) values (%s, %s)', ['1', 'Jack'])
cursor.execute('insert into user (id, name) values (%s, %s)', ['2', 'Chilly'])
cursor.execute('insert into user (id, name) values (%s, %s)', ['3', 'Jack2'])
# 返回表数据行数
print(cursor.rowcount)
# 提交事务
conn.commit()
cursor.close()
# 查询数据
cursor = conn.cursor()
cursor.execute('select * from user where id = %s', ('1',))
values = cursor.fetchall()
print(values)
# 关闭数据库
cursor.close()
conn.close()