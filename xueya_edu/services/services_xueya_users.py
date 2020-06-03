#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from models.model_xueya_users import User

user = User()


def get_all_users():
    try:
        all_users = user.get_all_users()
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
    except Exception as e:
        raise e


def get_users():
    all_users = get_all_users()
    users = filter(lambda item: item['isDeleted'] == 'N', all_users)
    return users


def set_new_user(new_user):
    try:
        user.set_new_user(new_user)
        uid = user.get_id_by_account_name(new_user)
        return uid
    except Exception as e:
        raise e


def delete_user(id_dict):
    try:
        return user.delete_user_by_uid(id_dict)
    except Exception as e:
        raise e
