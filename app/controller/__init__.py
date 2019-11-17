from flask import Flask
from app.controller.demo import demo
from app.controller.start import start
from app.controller.user import user
from app.controller.notice import notice
from app.controller.assets import assets
from app.middleware.user_check import jwt_middleware


def register_routes(app: Flask):
    app.register_blueprint(demo, url_prefix='/demo')
    app.register_blueprint(start, url_prefix='/start')
    jwt_middleware(user)
    app.register_blueprint(user, url_prefix='/user')
    jwt_middleware(notice)
    app.register_blueprint(notice, url_prefix='/notice')
    jwt_middleware(assets)
    app.register_blueprint(assets, url_prefix='/assets')

