#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from flask import jsonify, Blueprint, request
from json import dumps
from models.m_xueya_users import User
from services.s_xueya_users import get_all_users, get_users

user = User()
# 注册蓝图
r_users = Blueprint('users', __name__)


@r_users.route('/getAllUsers/', methods=['GET', 'POST'])
def get_all_user_info():
    return jsonify(get_all_users())


@r_users.route('/getUsers/', methods=['GET', 'POST'])
def get_user_info():
    return jsonify(list(get_users()))


@r_users.route('/addNewUser/', methods=['POST'])
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
    user.set_new_user(tuple(form_data.values()))
    uid = user.get_id_by_account_name(tuple(form_data.values()))
    return dumps(uid)
