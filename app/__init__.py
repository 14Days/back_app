from flask import Flask
from app.controller import register_routes


def create_app():
    app = Flask(__name__)
    # 添加配置
    app.config.from_object('app.settings.DevelopingConfig')
    # 注册蓝图
    register_routes(app)
    return app
