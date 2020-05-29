#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from mysql.connector import connect
from flask import Flask, request, jsonify

app = Flask(__name__)

# 连接数据库
conn = connect(user='root', password='root', database='db_xueya_edu')
cursor = conn.cursor()

cursor.execute('select * from xueya_users')
data = cursor.fetchall()
jsonData = []
for row in data:
    res = {
       'nickname': row[0],
       'idCard': row[1],
       'age': row[2],
       'profession': row[3],
       'address': row[4],
       'password': row[5],
       'avator': row[6],
       'wechat': row[7],
       'qq': row[8],
       'phone': row[9],
       'child_age': row[10],
       'message': row[11],
       'email': row[12]
    }
    jsonData.append(res)

print(jsonData)

# 关闭数据库
cursor.close()
conn.close()


@app.route('/', methods=['GET', 'POST'])
def get_user_info():
    # return json.dumps(users, ensure_ascii=False)
    return jsonify(jsonData)


if __name__ == '__main__':
    app.run()
