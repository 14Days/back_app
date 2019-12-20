from app.model.define import Color
from app.util.exception import CommonException


def find_tag(color_id: int) -> list:
    color = Color.query.filter_by(id=color_id).first()
    if color is None:
        raise CommonException("用户尚未选择颜色")
    li = []
    for temp in color.second_tag:
        li.append(temp.id)
    return li
