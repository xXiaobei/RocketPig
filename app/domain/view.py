# encoding:utf-8
# 网站视图

from flask import Blueprint, render_template

dom_blue = Blueprint('dom_blue', __name__)  # 创建蓝图


@dom_blue.route('/')
def index():
    return render_template('domain/index.html')
