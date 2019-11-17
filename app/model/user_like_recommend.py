from app.model.define import AppUser, Recommend
from app.model import db
from app.util.exception import CommonException


def post_like(user_id, recommend_id):
    user = AppUser.query.filter_by(id=user_id).first()
    recommend = Recommend.query.filter_by(id=recommend_id).first()
    if recommend in user.likes:
        raise CommonException('已点赞过该图片')
    user.likes.append(recommend)
    db.session.add(user)
    db.session.commit()


def delete_like(user_id, recommend_id):
    user = AppUser.query.filter_by(id=user_id).first()
    recommend = Recommend.query.filter_by(id=recommend_id).first()
    if recommend not in user.likes:
        raise CommonException('还未点赞该图片')
    user.likes.remove(recommend)
    db.session.commit()
