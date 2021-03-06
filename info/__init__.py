from flask import Flask
# 导入flask_sqlalchemy扩展
from flask_sqlalchemy import SQLAlchemy

from flask_session import Session
from flask_wtf import CSRFProtect
# 导入日志模块
import logging
from logging.handlers import RotatingFileHandler




# 导入配置对象
from config import config

# sqlalchemy 数据库实例
db = SQLAlchemy()



# # 集成项目日志
# # 设置日志的记录等级
# logging.basicConfig(level=logging.DEBUG) # 调试bug级
# # 创建日志记录器，指明日志保存的路径，每个日志文件的最大大小，保存的日志文件个数上限
# file_log_handler = RotatingFileHandler('logs/log', maxBytes=1024*1024*100, backupCount=10)
# # 创建日志记录的格式 日志等级 输入日志信息的文件名 行数 日志信息
# formatter = logging.Formatter('%(levelname)s %(filename)s:%(lineno)d %(message)s')
# # 为刚创建的日志记录器设置日志记录格式
# file_log_handler.setFormatter(formatter)
# # 为全局的日志工具对象（flask app使用的）添加日志记录器
# logging.getLogger().addHandler(file_log_handler)



# 创建程序实例的工厂方法，动态的加载配置对象
def create_app(config_name):
    app = Flask(__name__)
    # 使用配置对象
    app.config.from_object(config[config_name])
    # 实例化session对象
    Session(app)
    # 实例化CSRF,实现跨站请求保护
    CSRFProtect(app)


    # 注册蓝图对象到app上
    from info.modules.news import news_blu
    app.register_blueprint(news_blu)

    return app























