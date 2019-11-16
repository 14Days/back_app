from app.model.define import AppUser, Recommend
from app.model import db


def post_collect(user_id: int, recommend_id: int):
    user = AppUser.query.filter_by(id=user_id).first()
    recommend = Recommend.query.filter_by(id=recommend_id).first()
    user.recommends.append(recommend)
    db.session.add(user)
    db.session.commit()
