from flask import Blueprint
from app.util.response import success_res
from app.model.notice import get_notice

notice = Blueprint('notice', __name__)


@notice.route('', methods=['GET'])
def return_notice():
    return success_res(get_notice())
