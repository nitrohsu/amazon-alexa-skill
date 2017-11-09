#!/usr/bin/python
# -*- coding: utf-8 -*-
from enum import Enum


class ResponseType(Enum):
    OutputSpeech = "outputSpeech"
    Card = "card"
    Reprompt = "reprompt"
    Directives = "directives"


class SpeechResponseType(Enum):
    PlainText = "PlainText"
    SSML = "SSML"


class CardResponseType(Enum):
    Simple = "Simple"
    Standard = "Standard"
    LinkAccount = "LinkAccount"


class BaseResponse(object):
    def __init__(self, resp_type):
        self._resp_type = resp_type

    @property
    def resp_type(self):
        return self._resp_type

    @resp_type.setter
    def resp_type(self, resp_type):
        self._resp_type = resp_type


class SpeechResponse(BaseResponse):
    def __init__(self, speech_type, text=None, ssml=None):
        super().__init__(ResponseType.OutputSpeech)
        if speech_type is None:
            speech_type = SpeechResponseType.PlainText.value
        if isinstance(speech_type, Enum):
            speech_type = SpeechResponseType.PlainText.value

        self._speech_type = speech_type
        self._text = text
        self._ssml = ssml

    @property
    def speech_type(self):
        return self._speech_type

    @speech_type.setter
    def speech_type(self, speech_type):
        self._speech_type = speech_type

    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, text):
        self._text = text

    @property
    def ssml(self):
        return self._ssml

    @ssml.setter
    def ssml(self, ssml):
        self._ssml = ssml

    def json_response(self):
        return {'type': self.speech_type, 'text': self.text, 'ssml': self.ssml}


class CardResponse(BaseResponse):
    def __init__(self, card_type, title, content, text, small_image_url, large_image_url):
        super().__init__(ResponseType.Card)
        if card_type is None:
            card_type = CardResponseType.Simple
        self._card_type = card_type
        self._title = title
        self._content = content
        self._text = text
        self._small_image_url = small_image_url
        self._large_image_url = large_image_url

    @property
    def card_type(self):
        return self._card_type

    @card_type.setter
    def card_type(self, card_type):
        self._card_type = card_type

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        self._title = title

    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, content):
        self._content = content

    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, text):
        self._text = text

    @property
    def small_image_url(self):
        return self._small_image_url

    @small_image_url.setter
    def small_image_url(self, small_image_url):
        self._small_image_url = small_image_url

    @property
    def large_image_url(self):
        return self._large_image_url

    @large_image_url.setter
    def large_image_url(self, large_image_url):
        self._large_image_url = large_image_url

    def json_response(self):
        return {'type': self.card_type, 'title': self.title, 'content': self.content, 'text': self.text,
                'image': {'smallImageUrl': self.small_image_url, 'largeImageUrl': self.large_image_url}}


class RepromptResponse(BaseResponse):
    def __init__(self, speech_response):
        super().__init__(ResponseType.Reprompt)
        self._speech_response = speech_response

    @property
    def speech_response(self):
        return self._speech_response

    @speech_response.setter
    def speech_response(self, speech_response):
        self._speech_response = speech_response

    def json_response(self):
        if self.speech_response:
            data = self.speech_response.json_response()
            return {'outputSpeech': {data}}
        else:
            return {'outputSpeech': {}}
