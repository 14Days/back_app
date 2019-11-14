from app.model import db
from app.model.define import AppUser
from app.util.exception import RegisterException
from app.util.md5 import encode_md5
from app.util.exception import LoginException


def add_user(username: str, password: str, phone: str):
    res = AppUser.query.filter_by(username=username).first()
    if res is not None:
        raise RegisterException('用户名已存在')
    password = encode_md5(password)
    user = AppUser(username=username, password=password, phone=phone)
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
