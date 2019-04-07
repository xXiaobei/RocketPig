# encoding:utf-8
# 工程视图

from flask import Blueprint, render_template

pro_blue = Blueprint('pro_blue', __name__)


@pro_blue.route('/')
def index():
    return render_template('index.html')
