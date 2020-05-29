#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Users:
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            self[k] = v
        # self.u_nickname = kwargs.u_nickname
        # self.u_id_card = kwargs.u_id_card
        # self.u_age = kwargs.u_age
        # self.u_profession = kwargs.u_profession
        # self.u_address = kwargs.u_address
        # self.u_password = kwargs.u_password
        # self.u_avator = kwargs.u_avator
        # self.u_wechat = kwargs.u_wechat
        # self.u_qq = kwargs.u_qq
        # self.u_phone = kwargs.u_phone
        # self.u_child_age = kwargs.u_child_age
        # self.u_message = kwargs.u_message
        # self.u_email = kwargs.u_email
