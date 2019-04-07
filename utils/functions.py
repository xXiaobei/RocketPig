# encoding:utf-8
# 公用函数封装

from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_session import Session

db = SQLAlchemy()
bt = Bootstrap()
se = Session()


# 初始化第三方扩展
def init_ext(app):
    db.init_app(app)
    bt.init_app(app)
    se.init_app(app)


# 开发数据库路径
def get_dev_dburi():
    return 'sqlite:///rocketpig.db'


# 生产数据库路径
def get_prc_dburi():
    database = 'mysql'  # 数据库类型
    driver = 'pymysql'
    host = '127.0.0.1'
    port = '3306'
    user = ''
    password = ''
    name = 'rocketpig'  # 数据库名
    return '{}+{}://{}:{}@{}:{}/{}'.format(database, driver, user, password, host, port, name)
