#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from mysql.connector import connect
from flask import Flask, request, jsonify

app = Flask(__name__)

# 连接数据库
conn = connect(user='root', password='root', database='db_xueya_edu')
cursor = conn.cursor()

cursor.execute('select * from xueya_users where is_deleted="N"')
data = cursor.fetchall()
jsonData = []
for row in data:
    res = {
       'nickname': row[1],
       'idCard': row[2],
       'age': row[3],
       'profession': row[4],
       'address': row[5],
       'password': row[6],
       'avator': row[7],
       'wechat': row[8],
       'qq': row[9],
       'phone': row[10],
       'child_age': row[11],
       'message': row[12],
       'email': row[13]
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
