from app.model.define import Notice
from app.model.avatar import get_web_avatar
from app.util.data_time import shift_time


def get_notice() -> list:
    res = Notice.query.filter_by(type=2).order_by(Notice.is_top.desc()).order_by(Notice.create_at.desc()).all()
    li = []
    for item in res:
        user = item.who
        li.append({
            'create_at': shift_time(str(item.create_at)),
            'content': item.content,
            'avatar': get_web_avatar(user.id)
        })
    return li
