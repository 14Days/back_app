from flask import Flask
from app.controller.demo import demo
from app.controller.start import start
from app.controller.user import user


def register_routes(app: Flask):
    app.register_blueprint(demo, url_prefix='/demo')
    app.register_blueprint(start, url_prefix='/start')
    app.register_blueprint(user, url_prefix='/user')
