from flask import Flask
# 导入扩展flas_script
from flask_script import Manager
# 导入flask_sqlalchemy扩展
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate,MigrateCommand
app = Flask(__name__)

# sqlalchemy 数据库实例
db = SQLAlchemy(app)
# 实例化管理器对象
manage = Manager(app)
# 使用迁移框架
Migrate(app,db)
# 通过管理器对象，添加迁移命令
manage.add_command("db",MigrateCommand)


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    manage.run()
