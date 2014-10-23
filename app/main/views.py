# -*- coding: utf-8 -*-
__author__ = 'florije'
from .import main


@main.route('/')
def index():
    return 'index.'


@main.route('/test')
def test():
    a = 1 / 0
    return a