import jwt
import time
from app.util.redis import red


def create_token(user_id: int) -> str:
    payload = {
        'user_id': user_id,
        'exp': time.time() + 6 * 24 * 60 * 60,
    }

    return str(jwt.encode(payload, 'secret', 'HS256'), encoding='utf-8')


def parse_token(token: str) -> dict:
    token = bytes(token, encoding='utf-8')
    return jwt.decode(token, 'secret', 'HS256')


def set_jwt_in_redis(user_id: int, token: str):
    red.connection.set(user_id, token)
    # 设置过期时间为6小时
    red.connection.expire(user_id, 6 * 24 * 60 * 60)