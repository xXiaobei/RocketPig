# encoding:utf-8

# 工程入口文件

from utils.app import create_app

app = create_app('default')  # 工厂函数，创建app

if __name__ == '__main__':
    app.run()
