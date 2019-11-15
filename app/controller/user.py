from flask import Blueprint, request, g, current_app
from app.model.color import get_color_list
from app.util.response import fail_res, success_res
from app.model.user_color import post_color, get_color
from app.model.user import get_user_info, post_user_info, change_password, delete_jwt_in_redis
from app.util.exception import DataBaseException, CommonException

user = Blueprint('user', __name__)


@user.route('/color', methods=['GET', 'POST'])
def color():
    if request.method == 'GET':
        return success_res(get_color_list())
    if request.method == 'POST':
        data = request.json
        user_id = g.user_id
        color_id = data.get('color_id')
        post_color(user_id, color_id)
        return success_res('提交成功')


@user.route('/info', methods=['GET', 'POST'])
def info():
    if request.method == 'GET':
        try:
            data = get_user_info(user_id=g.user_id)
            user_color = get_color(user_id=g.user_id)
            data['color'] = user_color
            return success_res(data)
        except DataBaseException as e:
            current_app.logger.error(e.err_msg)
            return fail_res(e.err_msg)

    if request.method == 'POST':
        user_id = g.user_id
        data = request.json
        if data is None:
            return fail_res('参数缺失')
        email = data.get('email')
        sex = data.get('sex')
        nickname = data.get('nickname')
        post_user_info(user_id, sex, email, nickname)
        return success_res('编辑成功')


@user.route('/password', methods=['POST'])
def password():
    try:
        user_id = g.user_id
        data = request.json
        old_password = data.get('old_password')
        new_password = data.get('new_password')
        change_password(user_id, old_password, new_password)
        return success_res('修改成功')
    except CommonException as e:
        current_app.logger.error(e.err_msg)
        return fail_res(e.err_msg)


@user.route('/logout', methods=['POST'])
def logout():
    user_id = g.user_id
    delete_jwt_in_redis(user_id)
    return success_res('退出登录')
