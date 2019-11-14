from flask import Flask
from app.controller import register_routes
from app.config.logger import create_logger
from app.middleware.global_logger import create_global_logger
from app.util.redis import red


def create_app():
    app = Flask(__name__)
    # 添加配置
    app.config.from_object('app.config.settings.DevelopingConfig')
    # 配置日志
    create_logger(app)
    # 添加全局log
    create_global_logger(app)
    # 注册蓝图
    register_routes(app)
    # 连接redis
    red.connect_redis(app)
    return app
