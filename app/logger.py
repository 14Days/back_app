import logging
from pathlib import Path
from logging.handlers import TimedRotatingFileHandler
from flask import Flask


def create_logger(app: Flask):
    path = Path(__file__).parent.parent
    log_file = path / 'log/flask.log'

    handler = TimedRotatingFileHandler(filename=log_file, when='D', interval=1, backupCount=4,
                                       encoding='UTF-8', delay=False, utc=False)
    formatter = logging.Formatter('[%(asctime)s][%(filename)s:%(lineno)d][%(levelname)s][%(thread)d] - %(message)s')
    handler.setFormatter(formatter)
    handler.setLevel(level=logging.INFO)
    app.logger.addHandler(handler)
    app.logger.setLevel(level=logging.INFO)
