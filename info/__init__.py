from flask import Flask
# 导入flask_sqlalchemy扩展
from flask_sqlalchemy import SQLAlchemy
from config import config, Config
from flask_session import Session
from flask_wtf import CSRFProtect







# sqlalchemy 数据库实例
db = SQLAlchemy()


# 创建程序实例的工厂方法，动态的加载配置对象
def create_app(config_name):
    app = Flask(__name__)
    # 使用配置对象
    app.config.from_object(config[config_name])
    # 实例化session对象
    Session(app)
    # 实例化CSRF
    CSRFProtect(app)

    return app
