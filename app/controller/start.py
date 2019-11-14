import re
from flask import Blueprint, request, current_app
from app.util.message import send_message, create_random_code, store_code_in_redis
from app.util.exception import RegisterException
from app.util.response import success_res, fail_res

start = Blueprint('start', __name__)


@start.route('/code', methods=['GET'])
def send_code():
    try:
        phone = request.args.get('phone')
        if phone is None or phone == '':
            return fail_res('参数缺失')
        if not re.match(r"^1[35678]\d{9}$", phone):
            return fail_res('参数格式错误')
        code = create_random_code()
        store_code_in_redis(phone, code)
        send_message(phone, code)
        return success_res('短信发送成功')
    except ConnectionError:
        current_app.logger.info('redis请求失败')
        return fail_res('请求失败')
    except RegisterException as e:
        current_app.logger.error(e.err_msg)
        return fail_res(e.err_msg)
