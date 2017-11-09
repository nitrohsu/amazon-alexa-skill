#!/usr/bin/python
# -*- coding: utf-8 -*-


class Context(object):
    def __init__(self, device, application_id, user, api_end_point, audio_player=None):
        self._device = device
        self._application_id = application_id
        self._user = user
        self._api_end_point = api_end_point
        self._audio_player = audio_player

    @property
    def device(self):
        return self._device

    @device.setter
    def device(self, device):
        self._device = device

    @property
    def application_id(self):
        return self._application_id

    @application_id.setter
    def application_id(self, application_id):
        self._application_id = application_id

    @property
    def user(self):
        return self._user

    @user.setter
    def user(self, user):
        self._user = user

    @property
    def api_end_point(self):
        return self._api_end_point

    @api_end_point.setter
    def api_end_point(self, api_end_point):
        self._api_end_point = api_end_point

    @property
    def audio_player(self):
        return self._audio_player

    @audio_player.setter
    def audio_player(self, audio_player):
        self._audio_player = audio_player
