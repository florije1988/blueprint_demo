# -*- coding: utf-8 -*-
__author__ = 'florije'
from .import demo
from flask import jsonify, current_app
import simplejson
from flask import request


@demo.app_errorhandler(400)
def bad_request(error=None):
    message = {
        'status': 400,
        'message': 'Bad request: %s' % error
    }
    resp = jsonify(message)
    resp.status_code = 400
    current_app.logger.info('Bad request: %s' % error)

    return resp


@demo.app_errorhandler(404)
def not_found(error=None):
    message = {
        'status': 404,
        'message': 'Not Found: %s' % error
    }
    resp = jsonify(message)
    resp.status_code = 404
    current_app.logger.info('Not Found: %s' % error)

    return resp


@demo.app_errorhandler(500)
def internal_server_error(error=None):
    message = {
        'status': 500,
        'message': 'Internal Server Error: %s' % error
    }
    resp = jsonify(message)
    resp.status_code = 500
    current_app.logger.info('Internal Server Error: %s' % error)

    return resp


@demo.route('/')
def index():
    return 'index.'


@demo.route('/test')
def test():
    a = 1 / 0
    return a


@demo.route('/', methods=['POST'])
def login():
    if request.method == 'POST':
        raw_data = request.data
        if raw_data:
            json_data = simplejson.loads(raw_data)
            names = json_data.get('names')
            return names
            # if 'name' in json_data:
            # return json_data.get('name')
            # else:
            #     return 'No user in data.'
        else:
            return 'Invalid username/password.'


