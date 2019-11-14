import re
from flask import Blueprint, request, current_app
from app.util.message import send_message, create_random_code, store_code_in_redis, get_code_from_redis
from app.util.exception import RegisterException
from app.util.response import success_res, fail_res
from app.model.user import add_user

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


@start.route('/register', methods=['POST'])
def register():
    try:
        # json替换get_json()，减少函数调用
        data = request.json
        if data is None:
            return fail_res('参数缺失')
        # get函数替换字典查找，避免KeyError
        phone = data.get('phone')
        username = data.get('username')
        password = data.get('password')
        code = data.get('code')
        if phone is None or \
                username is None or password is None or \
                code is None:
            return fail_res('参数缺失')
        if not re.match(r"^1[35678]\d{9}$", phone):
            return fail_res('参数格式不正确')
        old_code = get_code_from_redis(phone)
        if old_code is None:
            return fail_res('验证码过期')
        if code == str(old_code, encoding='utf-8'):
            add_user(username, password, phone)
            return success_res('注册成功')
        else:
            return fail_res('验证码错误')
        # 同级Error尽可能在同级处理，只有本级别无法处理再将Error抛出
    except RegisterException as e:
        current_app.logger.info(e.err_msg)
        return fail_res(e.err_msg)


# @start.route('login', methods=['POST'])
# def login():
#     data = request.json
#     if data is None:
#         return fail_res('参数缺失')
#     username = data.get('username')
