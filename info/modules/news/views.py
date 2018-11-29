from . import news_blu
from flask import session, render_template, current_app
# 使用蓝图对象



# 3------ 使用蓝图对象
# 访问首页并设置session信息
@news_blu.route("/")
def index():
    session["name"] = 'python1'
    return render_template('news/index.html')
#
@news_blu.route("/favicon.ico")
def favicon_image():
    # 使用应用
    return current_app.send_static_file('news/favicon.ico')











