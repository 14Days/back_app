from flask import Flask

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def connect_database(app: Flask):
    try:
        db.init_app(app)
        app.logger.info('Connect db successfully')
    except BaseException:
        app.logger.error('Failed to connect db')
