from app.model import db
from app.model.define import AppUser
from app.util.exception import RegisterException, CommonException
from app.util.md5 import encode_md5
from app.util.exception import LoginException
from app.util.redis import red


def add_user(username: str, password: str, phone: str):
    res = AppUser.query.filter_by(username=username).first()
    if res is not None:
        raise RegisterException('用户名已存在')
    password = encode_md5(password)
    user = AppUser(username=username, password=password, phone=phone, nickname=username)
    db.session.add(user)
    db.session.commit()


def check_phone(phone: str):
    res = AppUser.query.filter_by(phone=phone).first()
    if res is not None:
        raise RegisterException('手机号已存在')


def user_login(username: str, password: str) -> int:
    res = AppUser.query.filter_by(username=username).first()
    if res is None:
        raise LoginException('用户不存在')
    if res.password != password:
        raise LoginException('密码不正确')
    return res.id


def find_user(user_id: int) -> AppUser:
    res = AppUser.query.filter_by(id=user_id)
    return res.first()


def get_user_info(user_id: int) -> dict:
    res = AppUser.query.filter_by(id=user_id).first()
    return {
        'name': res.username,
        'phone': res.phone,
        'nickname': res.nickname,
        'sex': res.sex,
        'email': res.email
    }


def post_user_info(user_id: int, sex: int, email: str, nickname: str):
    user = AppUser.query.filter_by(id=user_id).first()
    user.sex = sex
    user.email = email
    user.nickname = nickname
    db.session.commit()


def change_password(user_id: int, old_password: str, new_password: str):
    old_password = encode_md5(old_password)
    res = AppUser.query.filter_by(id=user_id).first()
    if res.password != old_password:
        raise CommonException('密码错误')
    res.password = encode_md5(new_password)
    db.session.commit()


def delete_jwt_in_redis(user_id: int):
    red.connection.delete(user_id)
