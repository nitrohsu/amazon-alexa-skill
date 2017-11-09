#!/usr/bin/python
# -*- coding: utf-8 -*-
from enum import Enum

from model.response.Response import BaseResponse, ResponseType


class AudioPlayerDirective(Enum):
    Play = "AudioPlayer.Play"
    Stop = "AudioPlayer.Stop"
    ClearQueue = "AudioPlayer.ClearQueue"


class AudioPlayerPlayBehavior(Enum):
    REPLACE_ALL = "REPLACE_ALL"
    ENQUEUE = "ENQUEUE"
    REPLACE_ENQUEUED = "REPLACE_ENQUEUED"


class AudioPlayerClearBehavior(Enum):
    CLEAR_ENQUEUED = "CLEAR_ENQUEUED"
    CLEAR_ALL = "CLEAR_ALL"


class BaseDirective(BaseResponse):
    def __init__(self, directive):
        super().__init__(ResponseType.Directives)
        self._directive = directive

    @property
    def directive(self):
        return self._directive

    @directive.setter
    def directive(self, directive):
        self._directive = directive

    def json_response(self):
        return {'type': self.directive()}


# {
#   "type": "AudioPlayer.Play",
#   "playBehavior": "string",
#   "audioItem": {
#     "stream": {
#       "url": "string",
#       "token": "string",
#       "expectedPreviousToken": "string",
#       "offsetInMilliseconds": 0
#     }
#   }
# }
class AudioPlayerPlayDirective(BaseDirective):
    def __init__(self, play_behavior, url, token=None, expected_previous_token=None,
                 offset_in_milliseconds=0):
        super().__init__(AudioPlayerDirective.Play)
        self._play_behavior = play_behavior
        self._url = url
        self._token = token
        self._expected_previous_token = expected_previous_token
        self._offset_in_milliseconds = offset_in_milliseconds

        assert self._play_behavior is AudioPlayerPlayBehavior.ENQUEUE.value and self._expected_previous_token
        assert self._play_behavior is not AudioPlayerPlayBehavior.REPLACE_ALL.value and self._expected_previous_token

    @property
    def play_behavior(self):
        return self._play_behavior

    @play_behavior.setter
    def play_behavior(self, play_behavior):
        self._play_behavior = play_behavior

    @property
    def url(self):
        return self._url

    @url.setter
    def url(self, url):
        self._url = url

    @property
    def token(self):
        return self._token

    @token.setter
    def token(self, token):
        self._token = token

    @property
    def expected_previous_token(self):
        return self._expected_previous_token

    @expected_previous_token.setter
    def expected_previous_token(self, expected_previous_token):
        self._expected_previous_token = expected_previous_token

    @property
    def offset_in_milliseconds(self):
        return self._offset_in_milliseconds

    @offset_in_milliseconds.setter
    def offset_in_milliseconds(self, offset_in_milliseconds):
        self._offset_in_milliseconds = offset_in_milliseconds

    def json_response(self):
        data = super().json_response()
        data['playBehavior'] = self.play_behavior
        data['audioItem'] = {'stream': {}}
        data['audioItem']['stream']['url'] = self.url
        data['audioItem']['stream']['token'] = self.token
        if self.expected_previous_token == AudioPlayerPlayBehavior.ENQUEUE:
            data['audioItem']['stream']['expectedPreviousToken'] = self.expected_previous_token
        data['audioItem']['stream']['offsetInMilliseconds'] = self.offset_in_milliseconds
        return data


# {
#   "type": "AudioPlayer.Stop"
# }
class AudioPlayerStopDirective(BaseDirective):
    def __init__(self):
        super().__init__(AudioPlayerDirective.Stop)

    def json_response(self):
        return super().json_response()


# {
#   "type": "AudioPlayer.ClearQueue",
#   "clearBehavior" : "string"
# }
class AudioPlayerClearDirective(BaseDirective):
    def __init__(self, clear_behavior):
        super().__init__(AudioPlayerDirective.ClearQueue)
        self._clear_behavior = clear_behavior

    @property
    def clear_behavior(self):
        return self._clear_behavior

    @clear_behavior.setter
    def clear_behavior(self, clear_behavior):
        self._clear_behavior = clear_behavior

    def json_response(self):
        data = super().json_response()
        data['clearBehavior'] = self.clear_behavior
        return data
