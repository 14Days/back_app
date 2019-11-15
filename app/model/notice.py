from app.model.define import Notice


def get_notice() -> list:
    res = Notice.query.filter_by(type=2).all()
    li = []
    for item in res:
        li.append({
            'create_at': item.create_at,
            'content': item.content
        })
    return li

