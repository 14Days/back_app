from app.model.define import AppUser, AppAvatar
from app.model import db


def post_avatar(user_id: int, avatar_name):
    user = AppUser.query.filter_by(id=user_id).first()
    avatars = user.avatar
    if avatars is not None:
        for avatar in avatars:
            if avatar.status == 1:
                avatar.status = 2
    new_avatar = AppAvatar(name=avatar_name, status=1, user_id=user_id)
    avatars.append(new_avatar)
    db.session.commit()


def get_avatar(user_id: int):
    user = AppUser.query.filter_by(id=user_id).first()
    avatars = user.avatar
    for temp in avatars:
        if temp.status == 1:
            return temp.name

