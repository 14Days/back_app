from flask import Blueprint, request, g
from app.model.color import get_color_list
from app.util.response import fail_res, success_res
from app.model.user_color import post_color

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

