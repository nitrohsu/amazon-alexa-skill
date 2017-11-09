#!/usr/bin/python
# -*- coding: utf-8 -*-
from enum import Enum


class ConfirmationStatus(Enum):
    NONE = "NONE"
    CONFIRMED = "CONFIRMED"
    DENIED = "DENIED"


class Intent(object):
    def __init__(self, name, confirm_status=ConfirmationStatus.NONE, slots=None):
        if slots is None:
            slots = []
        self._name = name
        self._confirm_status = confirm_status
        self._slots = slots

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def confirm_status(self):
        return self._confirm_status

    @confirm_status.setter
    def confirm_status(self, confirm_status):
        self._confirm_status = confirm_status

    @property
    def slots(self):
        return self._slots

    @slots.setter
    def slots(self, slots):
        self._slots = slots


class Slot(object):
    def __init__(self, name, value, confirm_status=ConfirmationStatus.NONE, resolutions=None):
        if resolutions is None:
            resolutions = []
        self._name = name
        self._value = value
        self._confirm_status = confirm_status
        self._resolutions = resolutions

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value

    @property
    def confirm_status(self):
        return self._confirm_status

    @confirm_status.setter
    def confirm_status(self, confirm_status):
        self._confirm_status = confirm_status

    @property
    def resolutions(self):
        return self._resolutions

    @resolutions.setter
    def resolutions(self, resolutions):
        self._resolutions = resolutions


class Resolution(object):
    def __init__(self, authority, status_code, value_name_id_list=None):
        if value_name_id_list is None:
            value_name_id_list = []
        self._authority = authority
        self._status_code = status_code
        self._value_name_id_list = value_name_id_list

    @property
    def authority(self):
        return self._authority

    @authority.setter
    def authority(self, authority):
        self._authority = authority

    @property
    def status_code(self):
        return self._status_code

    @status_code.setter
    def status_code(self, status_code):
        self._status_code = status_code

    @property
    def value_name_id_list(self):
        return self._value_name_id_list

    @value_name_id_list.setter
    def value_name_id_list(self, value_name_id_list):
        self._value_name_id_list = value_name_id_list
