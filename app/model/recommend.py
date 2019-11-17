from app.model.define import Recommend, AppUser


def get_recommends(user_id: int, recommends_id: list) -> list:
    li = []
    for recommend_id in recommends_id:
        recommend = Recommend.query.filter_by(id=recommend_id).first()
        # 发布者
        user = recommend.who
        print(user)

        # 推荐消息包含的图片
        imgs = recommend.imgs
        imgs_name = []
        for img in imgs:
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

        li.append({
            'id': recommend_id,
            # 'name': user.username,
            'imgs_name': imgs_name,
            'sum_likes': sum_likes,
            'sum_collects': sum_collects,
            'content': recommend.content,
            'create_at': recommend.create_at,
            'designer_id': user.id,
            'is_followed': is_followed,
            'is_collected': is_collected,
            'is_liked': is_liked
        })
    return li
