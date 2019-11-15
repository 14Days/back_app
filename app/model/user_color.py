from flask import current_app
from app.model.define import AppUserColor
from app.model import db


def post_color(user_id: int, color_id: int):
    item = AppUserColor(app_user_id=user_id, color_id=color_id)
    res = AppUserColor.query.filter_by(app_user_id=user_id).first()
    if res is None:
        current_app.logger.info('新用户选择颜色')
    else:
        db.session.delete(res)
        db.session.commit()
    db.session.add(item)
    db.session.commit()