#!/usr/bin/python
# -*- coding: utf-8 -*-
from enum import Enum


class PlayerState(Enum):
    IDLE = "IDLE"
    PAUSED = "PAUSED"
    PLAYING = "PLAYING"
    BUFFER_UNDERRUN = "BUFFER_UNDERRUN"
    FINISHED = "FINISHED"
    STOPPED = "STOPPED"


class AudioPlayer(object):
    def __init__(self, token, offset_in_milliseconds, player_state):
        self._token = token
        self._offset_in_milliseconds = offset_in_milliseconds
        self._player_state = player_state

    @property
    def token(self):
        return self._token

    @token.setter
    def token(self, token):
        self._token = token

    @property
    def offset_in_milliseconds(self):
        return self._offset_in_milliseconds

    @offset_in_milliseconds.setter
    def offset_in_milliseconds(self, offset_in_milliseconds):
        self._offset_in_milliseconds = offset_in_milliseconds

    @property
    def player_state(self):
        return self._player_state

    @player_state.setter
    def player_state(self, player_state):
        self._player_state = player_state
