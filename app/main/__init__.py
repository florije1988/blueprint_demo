# -*- coding: utf-8 -*-
__author__ = 'florije'

from flask import Blueprint

main = Blueprint('main', __name__)

from app.main import views