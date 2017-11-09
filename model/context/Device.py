#!/usr/bin/python
# -*- coding: utf-8 -*-


class Device(object):
    def __init__(self, device_id, supported_interfaces=None):
        if supported_interfaces is None:
            supported_interfaces = []

        self._support_audio_player = supported_interfaces.get('AudioPlayer')
        self._device_id = device_id

    @property
    def device_id(self):
        return self._device_id

    @device_id.setter
    def device_id(self, device_id):
        self._device_id = device_id

    @property
    def support_audio_player(self):
        return self._support_audio_player

    @support_audio_player.setter
    def support_audio_player(self, support_audio_player):
        self._support_audio_player = support_audio_player
