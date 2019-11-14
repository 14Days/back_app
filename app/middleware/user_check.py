from flask import Blueprint, request, g, current_app
from redis import RedisError
from jwt.exceptions import ExpiredSignatureError, DecodeError
from app.util.redis import red
from app.util.response import fail_res
from app.util.jwt import parse_token


def jwt_middleware(app: Blueprint):
    @app.before_request
    def decode_token():
        token = request.headers.get('authorization')
        if token is None:
            current_app.logger.error('请携带jwt')
            return fail_res('请携带jwt'), 401

        try:
            jwt = parse_token(token)
            user_id = jwt['user_id']
            if red.connection.get(user_id) is None:
                current_app.logger.error('jwt不存在，请重新登录')
                return fail_res('jwt不存在，请重新登录'), 401
            g.user_id = user_id
            current_app.logger.info('当前登录用户id为%d', user_id)
        except ExpiredSignatureError:
            current_app.logger.error('jwt已过期，请重新登录')
            return fail_res('jwt已过期，请重新登录'), 401
        except DecodeError:
            current_app.logger.error('jwt错误')
            return fail_res('jwt错误'), 401
        except RedisError:
            current_app.logger.error('redis错误')
            return fail_res('redis错误'), 401
