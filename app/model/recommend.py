from app.model.define import Recommend, AppUser, User
from app.model.avatar import get_web_avatar
from app.util.data_time import shift_time


def get_recommends(user_id: int, recommends_id: list) -> list:
    li = []
    for recommend_id in recommends_id:
        recommend = Recommend.query.filter_by(id=recommend_id).first()
        if recommend.delete_at is not None:
            continue
        # 发布者
        user = recommend.who

        # 发布者头像
        avatar = get_web_avatar(user.id)

        # 推荐消息包含的图片
        imgs = recommend.imgs
        imgs_name = []
        for img in imgs:
            if img.delete_at is not None:
                continue
            imgs_name.append(img.name)

        # 点赞总数
        likers = recommend.likers
        sum_likes = len(likers)

        # 收藏总数
        collectors = recommend.collectors
        sum_collects = len(collectors)

        # 是否关注
        is_followed = False
        app_user = AppUser.query.filter_by(id=user_id).first()
        if user in app_user.followers:
            is_followed = True

        # 是否收藏
        is_collected = False
        if recommend in app_user.collects:
            is_collected = True

        # 是否点赞
        is_liked = False
        if recommend in app_user.likes:
            is_liked = True

        # 评论
        top_comments = recommend.top_comments
        top_li = []
        for top_comment in top_comments:
            if top_comment.delete_at is not None:
                continue
            top_commentor = top_comment.top_commentor
            second_comments = top_comment.second_comments
            second_li = []
            for second_comment in second_comments:
                if second_comment.delete_at is not None:
                    continue
                second_commentor = second_comment.second_commentor
                second_li.append({
                    'content': second_comment.content,
                    'create_at': shift_time(str(second_comment.create_at)),
                    'create_by': second_commentor.nickname
                })
            top_li.append({
                'id': top_comment.id,
                'content': top_comment.content,
                'create_at': shift_time(str(top_comment.create_at)),
                'create_by': top_commentor.nickname,
                'second_comment': second_li
            })

        li.append({
            'id': recommend_id,
            'name': user.username,
            'imgs_name': imgs_name,
            'avatar': avatar,
            'sum_likes': sum_likes,
            'sum_collects': sum_collects,
            'content': recommend.content,
            'create_at': shift_time(str(recommend.create_at)),
            'designer_id': user.id,
            'is_followed': is_followed,
            'is_collected': is_collected,
            'is_liked': is_liked,
            'top_comment': top_li
        })
    return li


def web_user_recommend(webs_id: list) -> list:
    li = []
    for web_id in webs_id:
        user = User.query.filter_by(id=web_id).first()
        recommends = user.recommends
        for recommend in recommends:
            li.append(recommend.id)
    return li


