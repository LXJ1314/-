# 创建新闻模块的蓝图对象
from flask import Blueprint

# 1------创建蓝图对象

news_blu = Blueprint("news_blu", __name__)



# 把使用蓝图对象的模块导入到创建蓝图对象的地方
from . import views