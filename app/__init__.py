# -*- coding: utf-8 -*-
__author__ = 'florije'

from flask import Flask
from config import config
# from demos.views import demo


def create_app(config_name):
    app = Flask(__name__)

    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    from app.main import main
    from app.demos import demo
    app.register_blueprint(demo, url_prefix='/demo')
    app.register_blueprint(main, url_prefix='/main')

    return app