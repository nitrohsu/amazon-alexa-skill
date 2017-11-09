#!/usr/bin/python
# -*- coding: utf-8 -*-


class Session(object):
    def __init__(self, session_id, new, application_id, attributes, user):
        if attributes is None:
            attributes = []
        self._session_id = session_id
        self._new = new
        self._application_id = application_id
        self._attributes = attributes
        self._user = user

    @property
    def session_id(self):
        return self._session_id

    @session_id.setter
    def session_id(self, session_id):
        self._session_id = session_id

    @property
    def new(self):
        return self._new

    @new.setter
    def new(self, new):
        self._new = new

    @property
    def application_id(self):
        return self._application_id

    @application_id.setter
    def application_id(self, application_id):
        self._application_id = application_id

    @property
    def attributes(self):
        return self._attributes

    @attributes.setter
    def attributes(self, attributes):
        self._attributes = attributes

    @property
    def user(self):
        return self._user

    @user.setter
    def user(self, user):
        self._user = user
