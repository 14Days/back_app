from app.model import db
from app.model.define import AppUser, User
from app.util.exception import CommonException


def post_follow(app_id: int, web_id: int):
    app_user = AppUser.query.filter_by(id=app_id).first()
    web_user = User.query.filter_by(id=web_id).first()
    if web_user is None:
        raise CommonException('相关用户不存在')
    web_user.app_users.append(app_user)
    db.session.add(web_user)
    db.session.commit()


def delete_follow(app_id: int, web_id: int):
    app_user = AppUser.query.filter_by(id=app_id).first()
    web_user = User.query.filter_by(id=web_id).first()
    if app_user not in web_user.app_users:
        raise CommonException('尚未关注该用户')
    web_user.app_users.remove(app_user)
    db.session.commit()


def get_follow(app_id: int) -> list:
    app_user = AppUser.query.filter_by(id=app_id).first()
    web_user = app_user.followers
    if len(web_user) == 0:
        raise CommonException('尚未关注用户')
    li = []
    for item in web_user:
        li.append(item.id)
    return li
