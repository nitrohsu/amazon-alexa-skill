#!/usr/bin/python
# -*- coding: utf-8 -*-
from enum import Enum


class RequestType(Enum):
    LaunchRequest = "LaunchRequest"
    IntentRequest = "IntentRequest"
    SessionEndedRequest = "SessionEndedRequest"

    AudioPlayerPlaybackStarted = "AudioPlayer.PlaybackStarted"
    AudioPlayerPlaybackFinished = "AudioPlayer.PlaybackFinished"
    AudioPlayerPlaybackStopped = "AudioPlayer.PlaybackStopped"
    AudioPlayerPlaybackNearlyFinished = "AudioPlayer.PlaybackNearlyFinished"
    AudioPlayerPlaybackFailed = "AudioPlayer.PlaybackFailed"

    PlaybackControllerNextCommandIssued = "PlaybackController.NextCommandIssued"
    PlaybackControllerPauseCommandIssued = "PlaybackController.PauseCommandIssued"
    PlaybackControllerPlayCommandIssued = "PlaybackController.PlayCommandIssued"
    PlaybackControllerPreviousCommandIssued = "PlaybackController.PreviousCommandIssued"
    PlaybackControllerReqException = "System.ExceptionEncountered"


class DialogState(Enum):
    STARTED = 'STARTED'
    IN_PROGRESS = 'IN_PROGRESS'
    COMPLETED = 'COMPLETED'


class Locale(Enum):
    EN_DE = 'de-DE'
    EN_GB = 'en-GB'
    EN_IN = 'en-IN'
    EN_US = 'en-US'


class SessionEndReason(Enum):
    USER_INITIATED = 'USER_INITIATED'
    ERROR = 'ERROR'
    EXCEEDED_MAX_REPROMPTS = 'EXCEEDED_MAX_REPROMPTS'


class SessionError(Enum):
    INVALID_RESPONSE = 'INVALID_RESPONSE'
    DEVICE_COMMUNICATION_ERROR = 'DEVICE_COMMUNICATION_ERROR'
    INTERNAL_ERROR = 'INTERNAL_ERROR'


# {
#   "type": "LaunchRequest",
#   "requestId": "string",
#   "timestamp": "string",
#   "locale": "string"
# }
class BaseRequest(object):
    def __init__(self, req_type=RequestType.LaunchRequest, req_id=None, timestamp=0, locale=Locale.EN_US):
        self._req_type = req_type
        self._req_id = req_id
        self._timestamp = timestamp
        self._locale = locale

    @property
    def req_type(self):
        return self._req_type

    @req_type.setter
    def req_type(self, req_type):
        self._req_id = req_type

    @property
    def req_id(self):
        return self._req_id

    @req_id.setter
    def req_id(self, req_id):
        self._req_id = req_id

    @property
    def timestamp(self):
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        self._timestamp = timestamp

    @property
    def locale(self):
        return self._locale

    @locale.setter
    def locale(self, locale):
        self._locale = locale


class LaunchRequest(BaseRequest):
    def __init__(self, req_id=None, timestamp=0, locale=Locale.EN_US):
        super().__init__(RequestType.LaunchRequest, req_id, timestamp, locale)


# {
#   "type": "IntentRequest",
#   "requestId": "string",
#   "timestamp": "string",

#   "dialogState": "string",
#   "locale": "string",
#   "intent": {
#     "name": "string",
#     "confirmationStatus": "string",
#     "slots": {
#       "SlotName": {
#         "name": "string",
#         "value": "string",
#         "confirmationStatus": "string",
#         "resolutions": {
#           "resolutionsPerAuthority": [
#             {
#               "authority": "string",
#               "status": {
#                 "code": "string"
#               },
#               "values": [
#                 {
#                   "value": {
#                     "name": "string",
#                     "id": "string"
#                   }
#                 }
#               ]
#             }
#           ]
#         }
#       }
#     }
#   }
# }
class IntentRequest(BaseRequest):
    def __init__(self, req_id=None, timestamp=None, locale=Locale.EN_US,
                 dialog_state=DialogState.STARTED, intent=None):
        super().__init__(RequestType.IntentRequest, req_id, timestamp, locale)

        self._dialog_state = dialog_state
        self._intent = intent

    @property
    def dialog_state(self):
        return self._dialog_state

    @dialog_state.setter
    def dialog_state(self, dialog_state):
        self._dialog_state = dialog_state

    @property
    def intent(self):
        return self._intent

    @intent.setter
    def intent(self, intent):
        self._intent = intent


# {
#   "type": "SessionEndedRequest",
#   "requestId": "string",
#   "timestamp": "string",
#   "reason": "string",
#   "locale": "string",
#   "error": {
#     "type": "string",
#     "message": "string"
#   }
# }
class SessionEndedRequest(BaseRequest):
    def __init__(self, req_id=None, timestamp=None, locale=Locale.EN_US,
                 reason=SessionEndReason.ERROR, error=SessionError.INTERNAL_ERROR, error_msg=None):
        super().__init__(RequestType.SessionEndedRequest, req_id, timestamp, locale)

        self._reason = reason
        self._error = error
        self._error_msg = error_msg

    @property
    def reason(self):
        return self._reason

    @reason.setter
    def reason(self, reason):
        self._reason = reason

    @property
    def error(self):
        return self._error

    @error.setter
    def error(self, error):
        self._error = error

    @property
    def error_msg(self):
        return self._error_msg

    @error_msg.setter
    def error_msg(self, error_msg):
        self._error_msg = error_msg


# {
#   "type": "AudioPlayer.PlaybackStarted",
#   "requestId": "string",
#   "timestamp": "string",
#   "token": "string",
#   "offsetInMilliseconds": 0,
#   "locale": "string"
# }
class AudioPlayerRequest(BaseRequest):
    def __init__(self, req_type, req_id=None, timestamp=None, locale=Locale.EN_US, token=None,
                 offset_in_milliseconds=0):
        super().__init__(req_type, req_id, timestamp, locale)
        self._token = token
        self._offset_in_milliseconds = offset_in_milliseconds

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


# {
#   "type": "PlaybackController.NextCommandIssued",
#   "requestId": "string",
#   "timestamp": "string",
#   "locale": "string"
# }
class PlaybackControllerRequest(BaseRequest):
    def __init__(self, req_type, req_id=None, timestamp=None, locale=Locale.EN_US):
        super().__init__(req_type, req_id, timestamp, locale)


# {
#   "type": "System.ExceptionEncountered",
#   "requestId": "string",
#   "timestamp": "string",
#   "locale": "string",
#   "error": {
#     "type": "string",
#     "message": "string"
#   },
#   "cause": {
#     "requestId": "string"
#   }
# }
class PlaybackCtrlExceptRequest(PlaybackControllerRequest):
    def __init__(self, req_type, req_id=None, timestamp=None, locale=Locale.EN_US,
                 error_code=SessionError.INTERNAL_ERROR, error_msg=None):
        super().__init__(req_type, req_id, timestamp, locale)
        self._error_code = error_code
        self._error_msg = error_msg

    @property
    def error_code(self):
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        self._error_code = error_code

    @property
    def error_msg(self):
        return self._error_msg

    @error_msg.setter
    def error_msg(self, error_msg):
        self._error_msg = error_msg
