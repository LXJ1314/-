from flask import Flask
# 导入扩展flas_script
from flask_script import Manager
# 导入扩展flask-migrate
from flask_migrate import Migrate, MigrateCommand
from info import create_app, db

app = create_app("development")


# 实例化管理器对象
manage = Manager(app)
# 使用迁移框架
Migrate(app, db)
# 通过管理器对象，添加迁移命令
manage.add_command("db", MigrateCommand)


@app.route('/')
def hello_world():
    return 'hello world'


if __name__ == '__main__':
    manage.run()
