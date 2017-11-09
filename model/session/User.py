#!/usr/bin/python
# -*- coding: utf-8 -*-


class User(object):
    def __init__(self, user_id, access_token, permissions=None):
        if permissions is None:
            permissions = []
        self._user_id = user_id
        self._access_token = access_token
        self._permissions = permissions

    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        self._user_id = user_id

    @property
    def access_token(self):
        return self._access_token

    @access_token.setter
    def access_token(self, user_access_token):
        self._access_token = user_access_token

    @property
    def permissions(self):
        return self._permissions

    @permissions.setter
    def permissions(self, permissions):
        self._permissions = permissions
