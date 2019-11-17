from app.model.define import SecondTag


def find_recommend(tags_id: list) -> list:
    li = []
    for tag_id in tags_id:
        tag = SecondTag.query.filter_by(id=tag_id).first()
        for recommend in tag.recommends:
            li.append(recommend.id)
    return li
