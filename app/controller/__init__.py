from flask import Flask
from app.controller.demo import demo
from app.controller.start import start


def register_routes(app: Flask):
    app.register_blueprint(demo, url_prefix='/demo')
    app.register_blueprint(start, url_prefix='/start')