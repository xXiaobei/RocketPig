# encoding:utf-8
# 资源视图

from flask import Blueprint, render_template

res_blue = Blueprint('res_blue', __name__)


@res_blue.route('/')
def index():
    return render_template('resource/index.html')
