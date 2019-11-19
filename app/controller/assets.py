from flask import Blueprint, g, current_app, request
from app.model.user_color import get_color
from app.model.color_find_tag import find_tag
from app.util.response import success_res, fail_res
from app.util.exception import DataBaseException, CommonException
from app.model.tag_find_recommend import find_recommend
from app.model.recommend import get_recommends, web_user_recommend
from app.model.user_follow_user import get_follow
from app.model.user_collect_recommend import get_collect

assets = Blueprint('assets', __name__)


@assets.route('/recommend')
def recommend():
    try:
        user_id = g.user_id
        color_id = get_color(user_id)
        tags_id = find_tag(color_id)
        recommends_id = find_recommend(tags_id)
        return success_res(get_recommends(user_id, recommends_id))
    except DataBaseException as e:
        current_app.logger.error(e.err_msg)
        return fail_res(e.err_msg)


@assets.route('/follow')
def follow():
    try:
        user_id = g.user_id
        web_user_id = get_follow(user_id)
        recommends_id = web_user_recommend(web_user_id)
        return success_res(get_recommends(user_id, recommends_id))
    except CommonException as e:
        current_app.logger.error(e.err_msg)
        return fail_res(e.err_msg)


@assets.route('/collect')
def collect():
    try:
        user_id = g.user_id
        recommends_id = get_collect(user_id)
        return success_res(get_recommends(user_id, recommends_id))
    except CommonException as e:
        current_app.logger.error(e.err_msg)
        return fail_res(e.err_msg)


@assets.route('/thing', methods=['POST'])
def thing():
    try:
        user_id = g.user_id
        data = request.json
        tags_id = data.get('tags_id')
        recommends_id = find_recommend(tags_id)
        return success_res(get_recommends(user_id, recommends_id))
    except DataBaseException as e:
        current_app.logger.error(e.err_msg)
        return fail_res(e.err_msg)
    except CommonException as e:
        current_app.logger.error(e.err_msg)
        return fail_res(e.err_msg)