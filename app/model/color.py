from app.model.define import Color


def get_color_list() -> list:
    res = Color.query.all()
    li = []
    for item in res:
        li.append({
            'color_id': item.id,
            'color': item.color
        })
    return li
