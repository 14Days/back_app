from app.controller.demo import demo
from flask import Flask


def register_routes(app: Flask):
    app.register_blueprint(demo)