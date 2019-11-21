import datetime
from app.model.define import TopComment, SecondComment
from app.model import db


def post_top_comment(app_user_id: int, recommend_id: id, content: str):
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(current_time)
    comment = TopComment(app_user_id=app_user_id, recommend_id=recommend_id, content=content, create_at=current_time)
    db.session.add(comment)
    db.session.commit()


def post_second_comment(app_user_id: int, top_comment_id: int, content: str):
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    second_commend = SecondComment(app_user_id=app_user_id, top_comment_id=top_comment_id, content=content,
                                   create_at=current_time)
    top_comment = TopComment.query.filter_by(id=top_comment_id).first()
    top_comment.second_comments.append(second_commend)
    db.session.commit()
