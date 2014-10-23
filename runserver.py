# -*- coding: utf-8 -*-
__author__ = 'florije'

from flask.ext.script import Manager
# from blueprint_demo import create_app
from app import create_app

app = create_app('development')
# manager = Manager(app)

if __name__ == '__main__':
    app.run()
    # manager.run()