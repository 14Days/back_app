from app.model.define import SecondTag
from app.util.exception import CommonException


def find_recommend(tags_id: list) -> list:
    li = []
    for tag_id in tags_id:
        print(tag_id)
        tag = SecondTag.query.filter_by(id=tag_id).first()
        if tag is None:
            raise CommonException('不存在该分类')
        if len(tag.recommends) == 0:
            raise CommonException('该分类未添加推荐消息')
        for recommend in tag.recommends:
            li.append(recommend.id)
    return li
