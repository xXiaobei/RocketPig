# falsk 脚本管理


# flask脚本管理，用于分离系统的相关脚本文件
from flask_script import Manager
# flask_migrate 用于数据库迁移的第三方插件
from flask_migrate import Migrate, MigrateCommand
from utils.app import create_app
from utils.functions import db

app = create_app('default')
migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

'''
# 数据库迁移用例 
# python manage.py db init   初始化数据库,会创建一个migations文件夹,并且会在数据库中生成一个alembic_version表
# python manage.py db migrate  创建迁移历史
# python manage.py db upgrade  更新数据库
'''

if __name__ == '__main__':
    manager.run()
