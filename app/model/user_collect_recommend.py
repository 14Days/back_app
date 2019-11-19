from app.model.define import AppUser, Recommend
from app.model import db
from app.util.exception import CommonException


def post_collect(user_id: int, recommend_id: int):
    user = AppUser.query.filter_by(id=user_id).first()
    recommend = Recommend.query.filter_by(id=recommend_id).first()
    if recommend in user.collects:
        raise CommonException('已收藏过该图片')
    user.collects.append(recommend)
    db.session.add(user)
    db.session.commit()


def delete_collect(user_id: int, recommend_id: int):
    user = AppUser.query.filter_by(id=user_id).first()
    recommend = Recommend.query.filter_by(id=recommend_id).first()
    if recommend not in user.collects:
        raise CommonException('还未收藏该图片')
    user.collects.remove(recommend)
    db.session.commit()


def get_collect(user_id: int) -> list:
    user = AppUser.query.filter_by(id=user_id).first()
    collects = user.collects
    if len(collects) == 0:
        raise CommonException('还未收藏图片')
    li = []
    for collect in collects:
        li.append(collect.id)
    return li
