# encoding:utf-8
# Flask工厂函数 Flask 初始化

from flask import Flask
from app.views import pro_blue
from app.domain.view import dom_blue
from app.resource.view import res_blue
from app.server.view import ser_blue
from config import configMap, STATIC_DIR, TEMPLATE_DIR
from utils.functions import init_ext


# 创建开发环境工程
def create_app(config_name):
    app = Flask(__name__, static_folder=STATIC_DIR, template_folder=TEMPLATE_DIR)
    app.config.from_object(configMap[config_name])  # 导入工程的配置文件

    # 注册蓝图
    app.register_blueprint(blueprint=pro_blue, url_prefix='')
    app.register_blueprint(blueprint=dom_blue, url_prefix='/domain')  # 添加蓝图前缀 url_prefix 为 /domain
    app.register_blueprint(blueprint=res_blue, url_prefix='/resource')
    app.register_blueprint(blueprint=ser_blue, url_prefix='/server')

    # 初始化地方方插件
    init_ext(app)

    return app
