#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import Flask, request, make_response
from flask import json

from model.context.Context import Context
from model.context.Device import Device
from model.player.AudioPlayer import AudioPlayer
from model.request.Intent import Intent, Resolution, Slot
from model.request.Request import RequestType, LaunchRequest, SessionEndedRequest, PlaybackCtrlExceptRequest, \
    IntentRequest, AudioPlayerRequest, PlaybackControllerRequest
from model.response.Directive import BaseDirective
from model.response.Response import SpeechResponse, SpeechResponseType, CardResponse, RepromptResponse
from model.session.Session import Session
from model.session.User import User

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def filter_all():
    headers = request.headers

    print("REQ Header:\n")
    for header in headers:
        print(header)
    print("\n")

    cookies = request.cookies

    print("REQ Cookie:\n")
    for cookie in cookies:
        print(cookie)
    print("\n")

    data = request.get_json()
    if data:
        context, session, req = parse_request(data)
        content = skill_in(context, session, req)
        response = skill_out(context, session, content)
        return json.jsonify(response)
    else:
        print("unknown request !!!")

    return make_response("HTTP ERROR!!! not json data", 403)


#
# 分流不同响应的处理
#
def parse_request(data):
    version = data['version']
    print("REQ version:\n" + json.dumps(version, sort_keys=True, indent=2, separators=(',', ':')) + '\n')
    session_dict = data['session']
    print("REQ session:\n" + json.dumps(session_dict, sort_keys=True, indent=2, separators=(',', ':')) + '\n')
    context = data['context']
    print("REQ context:\n" + json.dumps(context, sort_keys=True, indent=2, separators=(',', ':')) + '\n')
    req_dict = data['request']
    print("REQ request:\n" + json.dumps(req_dict, sort_keys=True, indent=2, separators=(',', ':')) + '\n')

    # application
    application = session_dict.get('application')
    application_id = None
    if application:
        application_id = application.get("applicationId", "")
    # user
    user_dict = session_dict.get('user')
    user = None
    if user_dict:
        user = User(user_dict.get('userId', ''), user_dict.get('accessToken', ''), user_dict.get('permissions', []))

    session = Session(session_dict.get('sessionId', ""), session_dict.get('new'), application_id,
                      session_dict.get('attributes', []), user)

    # context device
    device = Device(context.get('System').get('device').get('deviceId ', ''),
                    context.get('System').get('device').get('supportedInterfaces'))
    api_end_point = context.get('System').get('apiEndpoint')
    # context audio player
    audio_player_dict = context.get('AudioPlayer')
    audio_player = None
    if audio_player_dict:
        audio_player = AudioPlayer(context.get('AudioPlayer').get('token'),
                                   context.get('AudioPlayer').get('offsetInMilliseconds'),
                                   context.get('AudioPlayer').get('playerActivity'))

    context = Context(device, application_id, user, api_end_point, audio_player)

    # request
    alexa_req = None
    req_type = req_dict.get('type')
    if req_type:

        if RequestType.LaunchRequest.value == req_type:
            # LaunchRequest
            alexa_req = LaunchRequest(req_dict.get('requestId'), req_dict.get('timestamp'),
                                      req_dict.get('locale'))
        elif RequestType.SessionEndedRequest.value == req_type:
            # SessionEndedRequest
            err_dict = req_dict.get('error')
            err_type = err_msg = None
            if err_dict:
                err_type = err_dict.get('type')
                err_msg = err_dict.get('message')
            alexa_req = SessionEndedRequest(req_dict.get('requestId'), req_dict.get('timestamp'),
                                            req_dict.get('locale'), req_dict.get('reason'), err_type, err_msg)
        elif RequestType.IntentRequest.value == req_type:
            # IntentRequest
            intent_dict = req_dict.get('intent')
            if intent_dict:
                slot = None
                slots_dict = intent_dict.get('slots')
                if slots_dict:
                    for slot_name, slot_dict in slots_dict.items():
                        resolution = None
                        resolution_dict = slot_dict.get('resolutions')
                        if resolution_dict:
                            resolution_dict = resolution_dict.get('resolutionsPerAuthority')[0]
                            resolution = Resolution(resolution_dict.get('authority'),
                                                    resolution_dict.get('status').get('code'),
                                                    resolution_dict.get('values'))

                        slot = Slot(slot_dict.get('name'), slot_dict.get('value'), slot_dict.get('confirmationStatus'),
                                    resolution)
                intent = Intent(intent_dict.get('name'), intent_dict.get('confirmationStatus'), slot)
                alexa_req = IntentRequest(req_dict.get('requestId'), req_dict.get('timestamp'),
                                          req_dict.get('locale'), req_dict.get('dialogState'), intent)
        elif req_type and req_type.startswith('AudioPlayer.'):
            # AudioPlayer Requests
            alexa_req = AudioPlayerRequest(req_type, req_dict.get('requestId'), req_dict.get('timestamp'),
                                           req_dict.get('locale'), req_dict.get('token'),
                                           req_dict.get('offsetInMilliseconds'))
        elif req_type and req_type.startswith('PlaybackController.'):
            # PlaybackController Requests
            alexa_req = PlaybackControllerRequest(req_type, req_dict.get('requestId'), req_dict.get('timestamp'),
                                                  req_dict.get('locale'))
        elif req_type and req_type.startswith(RequestType.PlaybackControllerReqException.value):
            # PlaybackController Exception
            alexa_req = PlaybackCtrlExceptRequest(req_dict.get('requestId'),
                                                  req_dict.get('timestamp'),
                                                  req_dict.get('error').get('type'),
                                                  req_dict.get('error').get('message'))
    return context, session, alexa_req


def skill_in(context, session, req):
    if isinstance(req, LaunchRequest):
        return SpeechResponse(SpeechResponseType.PlainText, "Welcome to Hello PIN.")
    elif isinstance(req, SessionEndedRequest):
        return SpeechResponse(SpeechResponseType.PlainText, "Goodbye!")
    elif isinstance(req, IntentRequest):
        return SpeechResponse(SpeechResponseType.PlainText, "Hi,I'm intent response")
    else:
        return SpeechResponse(SpeechResponseType.PlainText, "Hi,I'm a player response")


def skill_out(context, session, content):
    content_dict = {}
    # TODO logic
    if isinstance(content, SpeechResponse):
        content_dict['outputSpeech'] = content.json_response()
    elif isinstance(content, CardResponse):
        content_dict['card'] = content.json_response()
    elif isinstance(content, RepromptResponse):
        content_dict['reprompt'] = content.json_response()
    elif isinstance(content, BaseDirective):
        content_dict['directives'] = (content.json_response())

    return {'version': '0.1', 'response': content_dict}


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=19090, debug=True)
