from app.model.define import SecondTag
from app.util.exception import CommonException


def find_recommend(tags_id: list) -> list:
    li = []
    is_null = 0
    for tag_id in tags_id:
        tag = SecondTag.query.filter_by(id=tag_id).first()
        if tag is None:
            raise CommonException('不存在该分类')
        if len(tag.recommends) == 0:
            is_null += 1
        for recommend in tag.recommends:
            li.append(recommend.id)

    if is_null == tags_id.__sizeof__():
        raise CommonException('尚未添加推荐消息')

    return li
