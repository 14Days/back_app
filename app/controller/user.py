from flask import Blueprint, request
from app.model.color import get_color_list
from app.util.response import fail_res, success_res

user = Blueprint('user', __name__)


@user.route('/color', methods=['GET', 'POST'])
def color():
    if request.method == 'GET':
        return success_res(get_color_list())

