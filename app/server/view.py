# encoding:utf-8
# 服务器视图

from flask import Blueprint, render_template

ser_blue = Blueprint('ser_blue', __name__)


@ser_blue.route('/')
def index():
    return render_template('server/index.html')
