import os

path = os.getcwd()


class DevelopingConfig:
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://designer:sEPL7PHYNk6DGpa2@wghtstudio.cn:3306/designer?charset=UTF8MB4'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    REDIS = {
        'password': 'gyk199941',
        'host': 'wghtstudio.cn',
        'port': 6379
    }


class ProductionConfig:
    DEBUG = False

