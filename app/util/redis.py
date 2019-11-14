from redis import Redis, ConnectionError
from flask import Flask


class Red:
    connection = None

    def connect_redis(self, app: Flask):
        try:
            config = app.config['REDIS']
            self.connection = Redis(host=config['host'], password=config['password'], port=config['port'])
            app.logger.info('redis连接成功')
        except ConnectionError:
            app.logger.error('redis连接失败')


red = Red()
