#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from mysql.connector import connect
from flask import Flask, request, jsonify
from json import dumps

app = Flask(__name__)


def db_close():
    conn, cursor = db_conn()
    # 关闭数据库
    cursor.close()
    conn.close()


def db_conn():
    # 连接数据库
    conn = connect(user='root', password='root', database='db_xueya_edu')
    cursor = conn.cursor()
    return conn, cursor


def model_get_all_users():
    conn, cursor = db_conn()
    cursor.execute('SELECT * FROM xueya_users')
    data = cursor.fetchall()
    conn.commit()
    db_close()
    return data


def model_set_new_users(new_user):
    conn, cursor = db_conn()
    sql = '''INSERT INTO xueya_users
            VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'''
    cursor.execute(sql, list(new_user))
    conn.commit()
    db_close()


def model_get_id_by_account_name(new_user):
    conn, cursor = db_conn()
    sql = 'SELECT u_id FROM xueya_users WHERE u_account_name = "%s"' % new_user[1]
    cursor.execute(sql)
    uid = cursor.fetchone()
    conn.commit()
    db_close()
    return uid[0]


def controller_get_all_users():
    all_users = model_get_all_users()
    json_data = []
    for row in all_users:
        res = {
            'account_name': row[1],
            'nickname': row[2],
            'idCard': row[3],
            'age': row[4],
            'profession': row[5],
            'address': row[6],
            'password': row[7],
            'avator': row[8],
            'wechat': row[9],
            'qq': row[10],
            'phone': row[11],
            'child_age': row[12],
            'message': row[13],
            'email': row[14],
            'isDeleted': row[15]
        }
        json_data.append(res)
    return json_data


def controller_get_users():
    all_users = controller_get_all_users()
    users = filter(lambda item: item['isDeleted'] == 'N', all_users)
    return users


@app.route('/getUsers/', methods=['GET', 'POST'])
def get_user_info():
    return jsonify(list(controller_get_users()))


@app.route('/getAllUsers/', methods=['GET', 'POST'])
def get_all_user_info():
    return jsonify(controller_get_all_users())


@app.route('/addNewUser/', methods=['POST'])
def set_user_info():
    form_data = dict(request.form)
    form_data = {
        'u_id': None,
        'u_account_name': form_data['accountName'],
        'u_nick_name': form_data['nickName'],
        'u_id_card': form_data['idCard'],
        'u_age': form_data['age'],
        'u_profession': form_data['profession'],
        'u_address': form_data['address'],
        'u_password': form_data['password'],
        'u_avator': form_data['avator'],
        'u_wechat': form_data['wechat'],
        'u_qq': form_data['qq'],
        'u_phone': form_data['phone'],
        'u_child_age': form_data['childAge'],
        'u_message': form_data['message'],
        'u_email': form_data['email'],
        'is_deleted': 'N'
    }
    model_set_new_users(tuple(form_data.values()))
    uid = model_get_id_by_account_name(tuple(form_data.values()))
    return dumps(uid)


if __name__ == '__main__':
    app.run()
