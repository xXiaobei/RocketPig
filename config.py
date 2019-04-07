# encoding:utf-8 项目的配置信息

import os
from utils.functions import get_dev_dburi, get_prc_dburi

BASEDIR = os.path.abspath(os.path.dirname(__file__))

STATIC_DIR = os.path.join(BASEDIR, 'static')

TEMPLATE_DIR = os.path.join(BASEDIR, 'templates')

# redis 配置 ？？
# PERMANENT_SESSION_LIFETIME seesion过期时间

# 配置节点基类
class Config(object):
    DEBUG: True  # 是否开启调试模式
    SECRET_KEY: os.urandom(20)
    SQLALCHEMY_DATABASE_URI: ''
    SQLALCHEMY_COMMIT_TEARDOWN: True
    SQLALCHEMY_TRACK_MODIFICATIONS: False  # 如果设置成 True (默认情况)，Flask-SQLAlchemy 将会追踪对象的修改并且发送信号。这需要额外的内存， 如果不必要的可以禁用它


# 开发环境配置
class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = get_dev_dburi()
    SQLALCHEMY_COMMIT_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    pass


# 生产环境配置
class ProductionConfig(Config):
    DEBUG = False
    SECRET_KEY = ''  # 生产环境中的密匙要设置为固定字符串，不然每次服务器启动密匙都改变，导致所有的session都失效
    SQLALCHEMY_DATABASE_URI = get_prc_dburi()


# 测试环境配置
class TestingConfig(Config):
    pass


configMap = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
