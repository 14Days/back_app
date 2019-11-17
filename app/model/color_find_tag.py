from app.model.define import Color


def find_tag(color_id: int) -> list:
    color = Color.query.filter_by(id=color_id).first()
    li = []
    for temp in color.second_tag:
        li.append(temp.id)
    return li
