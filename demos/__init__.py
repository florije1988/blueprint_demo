# -*- coding: utf-8 -*-
__author__ = 'florije'
from flask import Blueprint

demo = Blueprint('demo', __name__)

from . import views